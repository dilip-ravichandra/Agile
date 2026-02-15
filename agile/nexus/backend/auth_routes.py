from flask import Blueprint, request, jsonify, make_response
from models import (
    create_user, find_user_by_email, increment_login_attempts,
    reset_login_attempts, lock_account, create_wallet,
    save_password_reset, find_password_reset, increment_otp_attempts,
    delete_password_reset, update_user
)
from utils.password_utils import hash_password, verify_password
from utils.jwt_utils import generate_token
from utils.email_utils import send_otp_email
from config import Config
from datetime import datetime, timedelta
import random
import re

auth_bp = Blueprint('auth', __name__)

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """Validate password strength (min 8 chars, 1 uppercase, 1 lowercase, 1 number)"""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True

@auth_bp.route('/signup', methods=['POST'])
def signup():
    """User signup endpoint"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['fullName', 'email', 'password', 'phoneNumber', 
                         'university', 'skillsKnown', 'skillsToImprove', 'teachingComfort']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'{field} is required'}), 400
        
        # Validate email format
        if not validate_email(data['email']):
            return jsonify({'error': 'Invalid email format'}), 400
        
        # Validate password strength
        if not validate_password(data['password']):
            return jsonify({'error': 'Password must be at least 8 characters with uppercase, lowercase, and number'}), 400
        
        # Check if user already exists
        if find_user_by_email(data['email']):
            return jsonify({'error': 'Email already registered'}), 409
        
        # Hash password
        hashed_password = hash_password(data['password'])
        
        # Prepare user data
        user_data = {
            'fullName': data['fullName'].strip(),
            'email': data['email'].lower().strip(),
            'password': hashed_password,
            'phoneNumber': data['phoneNumber'].strip(),
            'university': data['university'].strip(),
            'skillsKnown': [skill.strip() for skill in data['skillsKnown'].split(',') if skill.strip()],
            'skillsToImprove': [skill.strip() for skill in data['skillsToImprove'].split(',') if skill.strip()],
            'teachingComfort': data['teachingComfort'],
            'teachingLevel': data.get('teachingLevel', None)
        }
        
        # Create user
        user_id = create_user(user_data)
        
        # Create wallet with starter tokens
        create_wallet(user_id)
        
        return jsonify({
            'message': 'User registered successfully',
            'userId': str(user_id)
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    """User login endpoint"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email and password are required'}), 400
        
        email = data['email'].lower().strip()
        password = data['password']
        
        # Find user
        user = find_user_by_email(email)
        if not user:
            return jsonify({'error': 'Invalid credentials'}), 401
        
        # Check if account is locked
        if user.get('accountLocked', False):
            return jsonify({'error': 'Account locked due to too many failed login attempts. Please reset your password.'}), 403
        
        # Verify password
        if not verify_password(password, user['password']):
            # Increment login attempts
            increment_login_attempts(email)
            
            # Check if should lock account
            attempts = user.get('loginAttempts', 0) + 1
            if attempts >= Config.MAX_LOGIN_ATTEMPTS:
                lock_account(email)
                return jsonify({'error': 'Account locked due to too many failed login attempts. Please reset your password.'}), 403
            
            remaining = Config.MAX_LOGIN_ATTEMPTS - attempts
            return jsonify({'error': f'Invalid credentials. {remaining} attempts remaining.'}), 401
        
        # Reset login attempts on successful login
        reset_login_attempts(email)
        
        # Generate JWT token
        token = generate_token(str(user['_id']))
        
        # Create response with HTTP-only cookie
        response = make_response(jsonify({
            'message': 'Login successful',
            'user': {
                'id': str(user['_id']),
                'fullName': user['fullName'],
                'email': user['email']
            }
        }))
        
        # Set HTTP-only cookie
        response.set_cookie(
            'token',
            token,
            httponly=True,
            secure=False,  # Set to True in production with HTTPS
            samesite='Lax',
            max_age=Config.JWT_EXPIRATION_HOURS * 3600
        )
        
        return response, 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """User logout endpoint"""
    try:
        response = make_response(jsonify({'message': 'Logout successful'}))
        response.set_cookie('token', '', expires=0)
        return response, 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    """Request password reset OTP"""
    try:
        data = request.get_json()
        
        if not data.get('email'):
            return jsonify({'error': 'Email is required'}), 400
        
        email = data['email'].lower().strip()
        
        # Check if user exists
        user = find_user_by_email(email)
        if not user:
            # Don't reveal if email exists or not for security
            return jsonify({'message': 'If the email exists, an OTP has been sent'}), 200
        
        # Generate 6-digit OTP
        otp = str(random.randint(100000, 999999))
        
        # Hash OTP before storing
        hashed_otp = hash_password(otp)
        
        # Calculate expiry time
        expiry = datetime.utcnow() + timedelta(minutes=Config.OTP_EXPIRY_MINUTES)
        
        # Save to database
        save_password_reset(email, hashed_otp, expiry)
        
        # Send OTP via email
        send_otp_email(email, otp)
        
        return jsonify({'message': 'OTP sent to your email'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/verify-otp', methods=['POST'])
def verify_otp():
    """Verify OTP for password reset"""
    try:
        data = request.get_json()
        
        if not data.get('email') or not data.get('otp'):
            return jsonify({'error': 'Email and OTP are required'}), 400
        
        email = data['email'].lower().strip()
        otp = data['otp'].strip()
        
        # Find password reset request
        reset_request = find_password_reset(email)
        if not reset_request:
            return jsonify({'error': 'No password reset request found'}), 404
        
        # Check if expired
        if datetime.utcnow() > reset_request['expiry']:
            delete_password_reset(email)
            return jsonify({'error': 'OTP has expired'}), 400
        
        # Check attempts
        if reset_request['attempts'] >= Config.MAX_OTP_ATTEMPTS:
            delete_password_reset(email)
            return jsonify({'error': 'Maximum OTP attempts exceeded'}), 400
        
        # Verify OTP
        if not verify_password(otp, reset_request['otp']):
            increment_otp_attempts(email)
            remaining = Config.MAX_OTP_ATTEMPTS - (reset_request['attempts'] + 1)
            return jsonify({'error': f'Invalid OTP. {remaining} attempts remaining.'}), 401
        
        return jsonify({'message': 'OTP verified successfully'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    """Reset password after OTP verification"""
    try:
        data = request.get_json()
        
        if not data.get('email') or not data.get('otp') or not data.get('newPassword'):
            return jsonify({'error': 'Email, OTP, and new password are required'}), 400
        
        email = data['email'].lower().strip()
        otp = data['otp'].strip()
        new_password = data['newPassword']
        
        # Validate password strength
        if not validate_password(new_password):
            return jsonify({'error': 'Password must be at least 8 characters with uppercase, lowercase, and number'}), 400
        
        # Find password reset request
        reset_request = find_password_reset(email)
        if not reset_request:
            return jsonify({'error': 'No password reset request found'}), 404
        
        # Verify OTP one more time
        if not verify_password(otp, reset_request['otp']):
            return jsonify({'error': 'Invalid OTP'}), 401
        
        # Check if expired
        if datetime.utcnow() > reset_request['expiry']:
            delete_password_reset(email)
            return jsonify({'error': 'OTP has expired'}), 400
        
        # Hash new password
        hashed_password = hash_password(new_password)
        
        # Update user password and unlock account
        update_user(email, {
            'password': hashed_password,
            'accountLocked': False,
            'loginAttempts': 0
        })
        
        # Delete password reset request
        delete_password_reset(email)
        
        return jsonify({'message': 'Password reset successful'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

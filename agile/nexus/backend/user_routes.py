from flask import Blueprint, request, jsonify
from models import find_user_by_id, get_wallet
from utils.jwt_utils import verify_token
from functools import wraps

user_bp = Blueprint('user', __name__)

def jwt_required(f):
    """JWT authentication decorator"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('token')
        
        if not token:
            return jsonify({'error': 'Authentication required'}), 401
        
        user_id = verify_token(token)
        if not user_id:
            return jsonify({'error': 'Invalid or expired token'}), 401
        
        request.user_id = user_id
        return f(*args, **kwargs)
    
    return decorated_function

@user_bp.route('/profile', methods=['GET'])
@jwt_required
def get_profile():
    """Get user profile"""
    try:
        user = find_user_by_id(request.user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        # Get wallet
        wallet = get_wallet(user['_id'])
        
        return jsonify({
            'user': {
                'id': str(user['_id']),
                'fullName': user['fullName'],
                'email': user['email'],
                'phoneNumber': user['phoneNumber'],
                'university': user['university'],
                'skillsKnown': user['skillsKnown'],
                'skillsToImprove': user['skillsToImprove'],
                'teachingComfort': user['teachingComfort'],
                'teachingLevel': user.get('teachingLevel'),
                'tokens': wallet['tokens'] if wallet else 0
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/tokens', methods=['GET'])
@jwt_required
def get_tokens():
    """Get user token balance"""
    try:
        user = find_user_by_id(request.user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        wallet = get_wallet(user['_id'])
        
        return jsonify({
            'tokens': wallet['tokens'] if wallet else 0
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

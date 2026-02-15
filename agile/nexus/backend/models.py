from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from config import Config
from datetime import datetime

# MongoDB Connection
try:
    client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
    # Test connection
    client.admin.command('ping')
    db = client[Config.DATABASE_NAME]
    
    # Collections
    users_collection = db['users']
    wallets_collection = db['wallets']
    password_resets_collection = db['password_resets']
    
    # Create unique index on email (only if it doesn't exist)
    try:
        users_collection.create_index('email', unique=True)
    except OperationFailure:
        pass  # Index already exists
        
    print("✓ Connected to MongoDB successfully")
except ConnectionFailure as e:
    print(f"✗ ERROR: Could not connect to MongoDB at {Config.MONGO_URI}")
    print(f"  Make sure MongoDB is installed and running.")
    print(f"  Error details: {str(e)}")
    raise SystemExit(1)
except Exception as e:
    print(f"✗ ERROR: Database initialization failed: {str(e)}")
    raise SystemExit(1)

def create_user(user_data):
    """Create a new user"""
    user_data['createdAt'] = datetime.utcnow()
    user_data['loginAttempts'] = 0
    user_data['accountLocked'] = False
    result = users_collection.insert_one(user_data)
    return result.inserted_id

def create_wallet(user_id):
    """Create wallet for user with starter tokens"""
    wallet_data = {
        'userId': user_id,
        'tokens': Config.STARTER_TOKENS,
        'createdAt': datetime.utcnow()
    }
    result = wallets_collection.insert_one(wallet_data)
    return result.inserted_id

def find_user_by_email(email):
    """Find user by email"""
    return users_collection.find_one({'email': email.lower()})

def find_user_by_id(user_id):
    """Find user by ID"""
    from bson.objectid import ObjectId
    return users_collection.find_one({'_id': ObjectId(user_id)})

def update_user(email, update_data):
    """Update user data"""
    return users_collection.update_one(
        {'email': email.lower()},
        {'$set': update_data}
    )

def increment_login_attempts(email):
    """Increment login attempts"""
    return users_collection.update_one(
        {'email': email.lower()},
        {'$inc': {'loginAttempts': 1}}
    )

def reset_login_attempts(email):
    """Reset login attempts to 0"""
    return users_collection.update_one(
        {'email': email.lower()},
        {'$set': {'loginAttempts': 0}}
    )

def lock_account(email):
    """Lock user account"""
    return users_collection.update_one(
        {'email': email.lower()},
        {'$set': {'accountLocked': True}}
    )

def get_wallet(user_id):
    """Get wallet by user ID"""
    from bson.objectid import ObjectId
    return wallets_collection.find_one({'userId': ObjectId(user_id)})

def save_password_reset(email, hashed_otp, expiry):
    """Save password reset request"""
    password_resets_collection.delete_many({'email': email.lower()})
    reset_data = {
        'email': email.lower(),
        'otp': hashed_otp,
        'expiry': expiry,
        'attempts': 0,
        'createdAt': datetime.utcnow()
    }
    return password_resets_collection.insert_one(reset_data)

def find_password_reset(email):
    """Find password reset by email"""
    return password_resets_collection.find_one({'email': email.lower()})

def increment_otp_attempts(email):
    """Increment OTP verification attempts"""
    return password_resets_collection.update_one(
        {'email': email.lower()},
        {'$inc': {'attempts': 1}}
    )

def delete_password_reset(email):
    """Delete password reset request"""
    return password_resets_collection.delete_one({'email': email.lower()})

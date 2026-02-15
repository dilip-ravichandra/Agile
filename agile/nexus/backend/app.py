from flask import Flask, send_from_directory
from flask_cors import CORS
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS for frontend
CORS(app, supports_credentials=True, origins=["http://localhost:5000", "http://127.0.0.1:5000"])

# Import routes
from auth_routes import auth_bp
from user_routes import user_bp

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(user_bp, url_prefix='/api/user')

# Serve frontend files
@app.route('/')
def serve_login():
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend')
    return send_from_directory(frontend_path, 'login.html')

@app.route('/<path:path>')
def serve_static(path):
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend')
    return send_from_directory(frontend_path, path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

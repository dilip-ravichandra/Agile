# 🚀 NEXUS - AI-Driven Knowledge Exchange Platform

<div align="center">

![NEXUS Banner](https://img.shields.io/badge/NEXUS-Knowledge%20Exchange-blueviolet?style=for-the-badge)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-green?style=for-the-badge&logo=mongodb)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**An innovative token-based knowledge exchange platform where every student can both teach and learn.**

[Features](#-features) • [Tech Stack](#-tech-stack) • [Installation](#-installation) • [API Documentation](#-api-documentation) • [Screenshots](#-screenshots)

</div>

---

## 📖 About

NEXUS is a revolutionary educational platform designed for Agile PBL (Project-Based Learning) that creates a collaborative ecosystem where students can:
- 🎓 **Share Knowledge** - Teach what you know to peers
- 📚 **Learn from Others** - Access quality content from fellow students
- 🪙 **Earn Tokens** - Get rewarded for teaching and contributing
- 🤝 **Build Community** - Connect with learners worldwide

## ✨ Features

### 🔐 Authentication System
- **Secure Signup** with comprehensive profile creation
- **JWT-based Authentication** with HTTP-only cookies
- **Password Security** using bcrypt hashing
- **Account Protection** with login attempt limits (5 attempts)
- **Forgot Password** with OTP-based recovery via email
- **Session Management** with automatic token expiration

### 👤 User Management
- Profile creation with skills tracking
- Teaching comfort level assessment
- Token-based wallet system
- Starter tokens (3) on signup
- Skill mapping (known vs. to-improve)

### 🏠 Dashboard
- Personalized welcome screen
- Real-time token balance display
- Skills visualization
- Teaching preference tracking
- Responsive navigation

### 🔒 Security Features
- **JWT Tokens** stored in HTTP-only cookies
- **Bcrypt Password Hashing** with salt
- **Environment Variables** for sensitive data
- **CORS Protection** with credential support
- **Input Validation** on all endpoints
- **Unique Email Enforcement** via MongoDB index
- **OTP Expiration** (5 minutes, 3 attempts max)

## 🛠 Tech Stack

### Backend
| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Core programming language |
| **Flask 3.0.0** | Web framework |
| **PyMongo 4.6.1** | MongoDB driver |
| **PyJWT 2.8.0** | JWT token generation |
| **Bcrypt 4.1.2** | Password hashing |
| **Flask-CORS 4.0.0** | Cross-origin resource sharing |
| **python-dotenv 1.0.0** | Environment variable management |

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients & glassmorphism
- **JavaScript (ES6+)** - Client-side logic & API communication

### Database
- **MongoDB** - NoSQL database for flexible schema
  - Collections: `users`, `wallets`, `password_resets`

## 📂 Project Structure

```
nexus/
│
├── backend/
│   ├── app.py                 # Flask application entry point
│   ├── config.py              # Configuration management
│   ├── auth_routes.py         # Authentication endpoints
│   ├── user_routes.py         # User management endpoints
│   ├── models.py              # Database models & operations
│   ├── utils/
│   │   ├── jwt_utils.py       # JWT token handling
│   │   ├── email_utils.py     # Email/OTP delivery
│   │   └── password_utils.py  # Password hashing utilities
│   ├── .env                   # Environment variables
│   └── requirements.txt       # Python dependencies
│
├── frontend/
│   ├── login.html             # Login page
│   ├── signup.html            # Signup page
│   ├── home.html              # User dashboard
│   ├── css/
│   │   └── styles.css         # Global styles
│   └── js/
│       ├── auth.js            # Authentication logic
│       └── home.js            # Dashboard logic
│
└── README.md                  # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- MongoDB installed and running
- Git (for cloning)

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/agile.git
cd agile/nexus
```

### Step 2: Install MongoDB
**Windows:**
```bash
# Download from: https://www.mongodb.com/try/download/community
# Install and start MongoDB service
```

**macOS:**
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

**Linux:**
```bash
sudo apt-get install mongodb
sudo systemctl start mongodb
```

### Step 3: Backend Setup
```bash
cd backend

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Configure Environment
Edit `backend/.env`:
```env
MONGO_URI=mongodb://localhost:27017/
JWT_SECRET=your_super_secret_key_here
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password
```

**📧 Gmail App Password Setup:**
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Security → 2-Step Verification → App Passwords
3. Generate password for "Mail"
4. Copy and paste into `EMAIL_PASS`

### Step 5: Run Application
```bash
cd backend
python app.py
```

Server will start at: **http://localhost:5000**

## 🎮 Usage

### Access Points
| Page | URL | Description |
|------|-----|-------------|
| **Login** | http://localhost:5000/login.html | User login |
| **Signup** | http://localhost:5000/signup.html | Create account |
| **Home** | http://localhost:5000/home.html | User dashboard |

### User Flow
1. **Sign Up** → Create account with email, password, skills
2. **Receive Tokens** → Get 3 starter tokens automatically
3. **Login** → Authenticate with credentials
4. **Dashboard** → View profile, tokens, skills
5. **Logout** → Secure session termination

## 📡 API Documentation

### Authentication Endpoints

#### POST `/api/auth/signup`
Create new user account.

**Request Body:**
```json
{
  "fullName": "John Doe",
  "email": "john@example.com",
  "password": "SecurePass123",
  "phoneNumber": "+1234567890",
  "university": "MIT",
  "skillsKnown": "Python, JavaScript, React",
  "skillsToImprove": "Machine Learning, DevOps",
  "teachingComfort": "YES",
  "teachingLevel": "INTERMEDIATE"
}
```

**Response:** `201 Created`
```json
{
  "message": "User registered successfully",
  "userId": "507f1f77bcf86cd799439011"
}
```

#### POST `/api/auth/login`
Authenticate user and create session.

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "SecurePass123"
}
```

**Response:** `200 OK` + HTTP-only cookie
```json
{
  "message": "Login successful",
  "user": {
    "id": "507f1f77bcf86cd799439011",
    "fullName": "John Doe",
    "email": "john@example.com"
  }
}
```

#### POST `/api/auth/logout`
Terminate user session.

**Response:** `200 OK`
```json
{
  "message": "Logout successful"
}
```

#### POST `/api/auth/forgot-password`
Request password reset OTP.

**Request Body:**
```json
{
  "email": "john@example.com"
}
```

**Response:** `200 OK`
```json
{
  "message": "OTP sent to your email"
}
```

#### POST `/api/auth/verify-otp`
Verify OTP code.

**Request Body:**
```json
{
  "email": "john@example.com",
  "otp": "123456"
}
```

#### POST `/api/auth/reset-password`
Reset password with OTP.

**Request Body:**
```json
{
  "email": "john@example.com",
  "otp": "123456",
  "newPassword": "NewSecurePass123"
}
```

### User Endpoints

#### GET `/api/user/profile`
Get authenticated user profile (requires JWT).

**Response:** `200 OK`
```json
{
  "user": {
    "id": "507f1f77bcf86cd799439011",
    "fullName": "John Doe",
    "email": "john@example.com",
    "phoneNumber": "+1234567890",
    "university": "MIT",
    "skillsKnown": ["Python", "JavaScript", "React"],
    "skillsToImprove": ["Machine Learning", "DevOps"],
    "teachingComfort": "YES",
    "teachingLevel": "INTERMEDIATE",
    "tokens": 3
  }
}
```

#### GET `/api/user/tokens`
Get user token balance (requires JWT).

**Response:** `200 OK`
```json
{
  "tokens": 3
}
```

## 🎨 Screenshots

### Login Page
- Clean glassmorphism design
- Forgot password modal
- Smooth animations

### Signup Page
- Comprehensive profile creation
- Dynamic teaching level selection
- Real-time validation

### Dashboard
- Welcome section with username
- Token balance display
- Skills visualization
- Responsive navigation bar

## 🔐 Security Best Practices

✅ **Passwords** - Bcrypt hashed with auto-generated salt  
✅ **JWT Tokens** - Stored in HTTP-only cookies (not localStorage)  
✅ **Environment Variables** - Sensitive data in `.env` file  
✅ **Input Validation** - Email, password strength checks  
✅ **Account Protection** - Login attempt limits & locking  
✅ **CORS** - Configured for specific origins  
✅ **MongoDB** - Unique indexes on sensitive fields  
✅ **OTP** - Time-limited (5 min) with attempt limits  

## 🗄️ Database Schema

### Users Collection
```javascript
{
  _id: ObjectId,
  fullName: String,
  email: String (unique, indexed),
  password: String (bcrypt hashed),
  phoneNumber: String,
  university: String,
  skillsKnown: Array[String],
  skillsToImprove: Array[String],
  teachingComfort: String (YES|NOT_SURE|NOT_NOW),
  teachingLevel: String (BEGINNER|INTERMEDIATE|ADVANCED|EXPERT),
  loginAttempts: Number,
  accountLocked: Boolean,
  createdAt: DateTime
}
```

### Wallets Collection
```javascript
{
  _id: ObjectId,
  userId: ObjectId (ref: Users),
  tokens: Number,
  createdAt: DateTime
}
```

### Password Resets Collection
```javascript
{
  _id: ObjectId,
  email: String,
  otp: String (bcrypt hashed),
  expiry: DateTime,
  attempts: Number,
  createdAt: DateTime
}
```

## 🌟 Future Enhancements

- [ ] **Content Marketplace** - Buy/sell courses with tokens
- [ ] **Live Sessions** - Real-time video teaching
- [ ] **AI Recommendations** - Smart skill matching
- [ ] **Reputation System** - Teacher ratings & reviews
- [ ] **Badges & Achievements** - Gamification elements
- [ ] **Mobile App** - React Native implementation
- [ ] **Social Features** - Follow, chat, groups
- [ ] **Analytics Dashboard** - Learning insights

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

**Agile PBL Project**  
Developed as part of Project-Based Learning initiative

## 📧 Contact

For questions or support, please open an issue or contact:
- Email: diliprbtech24@rvu.edu.in

## 🙏 Acknowledgments

- Flask documentation and community
- MongoDB documentation
- Bootstrap icons and design inspiration
- RV University for project support

---

<div align="center">

**⭐ Star this repo if you find it useful!**

Made with ❤️ for collaborative learning

</div>

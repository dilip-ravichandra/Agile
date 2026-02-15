<div align="center">

# ⚡ NEXUS

### 🌐 AI-Driven Token-Based Knowledge Exchange Platform

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=667EEA&center=true&vCenter=true&width=600&lines=Where+Every+Student+Can+Teach+%26+Learn;Token-Based+Knowledge+Exchange;Peer-to-Peer+Learning+Ecosystem;Built+for+the+Future+of+Education" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/)

<br/>

<img src="https://img.shields.io/github/stars/dilip-ravichandra/Agile?style=social" alt="Stars"/>
<img src="https://img.shields.io/github/forks/dilip-ravichandra/Agile?style=social" alt="Forks"/>
<img src="https://img.shields.io/github/issues/dilip-ravichandra/Agile?color=yellow" alt="Issues"/>
<img src="https://img.shields.io/github/license/dilip-ravichandra/Agile?color=green" alt="License"/>
<img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"/>

<br/><br/>

[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [📖 Documentation](#-api-documentation) • [🤝 Contributing](#-contributing)

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>

---

## 🎯 What is NEXUS?

<table>
<tr>
<td width="50%">

**NEXUS** is a revolutionary peer-to-peer learning platform that transforms how students share and acquire knowledge.

🎓 **Teach What You Know** — Share your expertise with peers

📚 **Learn What You Need** — Access quality content from fellow students

🪙 **Earn Tokens** — Get rewarded for your contributions

🤝 **Build Community** — Connect with learners worldwide

</td>
<td width="50%">

```
    ╔══════════════════════════════╗
    ║                              ║
    ║     🎓  STUDENT A           ║
    ║         │                    ║
    ║    Teaches Python            ║
    ║         │                    ║
    ║         ▼                    ║
    ║    🪙 Earns Tokens           ║
    ║         │                    ║
    ║         ▼                    ║
    ║    📚 Learns ML              ║
    ║         │                    ║
    ║         ▼                    ║
    ║     🎓  STUDENT B           ║
    ║                              ║
    ╚══════════════════════════════╝
```

</td>
</tr>
</table>

---

## ✨ Features

<div align="center">

| 🔐 **Authentication** | 👤 **User Management** | 🎨 **Modern UI** |
|:---:|:---:|:---:|
| JWT + HTTP-only Cookies | Token Wallet System | Glassmorphism Design |
| Bcrypt Password Hashing | Skills Tracking | Responsive Layout |
| OTP Password Recovery | Profile Management | Smooth Animations |
| Account Lock Protection | Teaching Preferences | Gradient Themes |

</div>

### 🔐 Secure Authentication System

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   📧 Email + Password ──► 🔒 Bcrypt Hash ──► ✅ JWT Token      │
│                                                                 │
│   🔑 Features:                                                  │
│   • HTTP-only cookie storage (XSS protection)                  │
│   • 5 login attempts before account lock                       │
│   • 6-digit OTP for password recovery                          │
│   • 5-minute OTP expiration                                    │
│   • Automatic session management                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 🪙 Token-Based Economy

<table>
<tr>
<td align="center" width="33%">

**🎁 Starter Bonus**
```
+3 Tokens
on Signup
```

</td>
<td align="center" width="33%">

**📚 Teaching Rewards**
```
Earn tokens by
sharing knowledge
```

</td>
<td align="center" width="33%">

**💡 Learning Access**
```
Spend tokens to
access content
```

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|:---:|:---|:---|
| 🎨 **Frontend** | HTML5, CSS3, JavaScript | Modern responsive UI with glassmorphism |
| ⚙️ **Backend** | Flask 3.0.0, Python 3.9+ | RESTful API server |
| 🔐 **Security** | JWT, Bcrypt | Authentication & password hashing |
| 🗄️ **Database** | MongoDB | NoSQL document storage |
| 📧 **Email** | SMTP (Gmail) | OTP delivery for password reset |

</div>

---

## 📁 Project Structure

```
nexus/
│
├── 🔧 backend/
│   ├── app.py                 # 🚀 Flask entry point
│   ├── config.py              # ⚙️ Configuration
│   ├── auth_routes.py         # 🔐 Auth endpoints
│   ├── user_routes.py         # 👤 User endpoints
│   ├── models.py              # 🗄️ Database models
│   ├── utils/
│   │   ├── jwt_utils.py       # 🔑 JWT handling
│   │   ├── email_utils.py     # 📧 Email/OTP
│   │   └── password_utils.py  # 🔒 Password hashing
│   ├── .env                   # 🔐 Environment vars
│   └── requirements.txt       # 📦 Dependencies
│
└── 🎨 frontend/
    ├── login.html             # 🔐 Login page
    ├── signup.html            # 📝 Signup page
    ├── home.html              # 🏠 Dashboard
    ├── css/
    │   └── styles.css         # 🎨 Styling
    └── js/
        ├── auth.js            # 🔐 Auth logic
        └── home.js            # 🏠 Dashboard logic
```

---

## 🚀 Quick Start

### Prerequisites

<table>
<tr>
<td>

**Required Software:**
- ✅ Python 3.9+
- ✅ MongoDB
- ✅ Git

</td>
<td>

**Recommended:**
- 📧 Gmail account (for OTP)
- 💻 VS Code editor

</td>
</tr>
</table>

### Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/dilip-ravichandra/Agile.git
cd Agile/nexus

# 2️⃣ Install Python dependencies
cd backend
pip install -r requirements.txt

# 3️⃣ Configure environment
# Edit .env file with your credentials

# 4️⃣ Start MongoDB (if not running)
# Windows: Start MongoDB service
# Mac: brew services start mongodb-community
# Linux: sudo systemctl start mongodb

# 5️⃣ Run the application
python app.py
```

### 🌐 Access the Application

| Page | URL |
|:---|:---|
| 🔐 **Login** | http://localhost:5000/login.html |
| 📝 **Signup** | http://localhost:5000/signup.html |
| 🏠 **Dashboard** | http://localhost:5000/home.html |

---

## ⚙️ Configuration

Create a `.env` file in the `backend/` directory:

```env
# 🗄️ MongoDB Connection
MONGO_URI=mongodb://localhost:27017/

# 🔐 JWT Secret (change in production!)
JWT_SECRET=your_super_secret_key_here

# 📧 Email Configuration (for OTP)
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password
```

<details>
<summary>📧 <b>How to get Gmail App Password</b></summary>

1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Navigate to **Security** → **2-Step Verification**
3. Scroll to **App Passwords**
4. Generate a new password for "Mail"
5. Copy and paste into `EMAIL_PASS`

</details>

---

## 📖 API Documentation

### 🔐 Authentication Endpoints

<details>
<summary><b>POST</b> <code>/api/auth/signup</code> — Create Account</summary>

**Request:**
```json
{
  "fullName": "John Doe",
  "email": "john@example.com",
  "password": "SecurePass123",
  "phoneNumber": "+1234567890",
  "university": "MIT",
  "skillsKnown": "Python, JavaScript",
  "skillsToImprove": "Machine Learning",
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
</details>

<details>
<summary><b>POST</b> <code>/api/auth/login</code> — Login</summary>

**Request:**
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
</details>

<details>
<summary><b>POST</b> <code>/api/auth/logout</code> — Logout</summary>

**Response:** `200 OK`
```json
{
  "message": "Logout successful"
}
```
</details>

<details>
<summary><b>POST</b> <code>/api/auth/forgot-password</code> — Request OTP</summary>

**Request:**
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
</details>

<details>
<summary><b>POST</b> <code>/api/auth/reset-password</code> — Reset Password</summary>

**Request:**
```json
{
  "email": "john@example.com",
  "otp": "123456",
  "newPassword": "NewSecurePass123"
}
```

**Response:** `200 OK`
```json
{
  "message": "Password reset successful"
}
```
</details>

### 👤 User Endpoints

<details>
<summary><b>GET</b> <code>/api/user/profile</code> — Get Profile</summary>

**Response:** `200 OK`
```json
{
  "user": {
    "id": "507f1f77bcf86cd799439011",
    "fullName": "John Doe",
    "email": "john@example.com",
    "tokens": 3,
    "skillsKnown": ["Python", "JavaScript"],
    "skillsToImprove": ["Machine Learning"]
  }
}
```
</details>

---

## 🗄️ Database Schema

```javascript
// 👤 Users Collection
{
  _id: ObjectId,
  fullName: String,
  email: String,        // unique index
  password: String,     // bcrypt hashed
  phoneNumber: String,
  university: String,
  skillsKnown: [String],
  skillsToImprove: [String],
  teachingComfort: "YES" | "NOT_SURE" | "NOT_NOW",
  teachingLevel: "BEGINNER" | "INTERMEDIATE" | "ADVANCED" | "EXPERT",
  loginAttempts: Number,
  accountLocked: Boolean,
  createdAt: DateTime
}

// 🪙 Wallets Collection
{
  _id: ObjectId,
  userId: ObjectId,
  tokens: Number,       // starts at 3
  createdAt: DateTime
}

// 🔑 Password Resets Collection
{
  _id: ObjectId,
  email: String,
  otp: String,          // bcrypt hashed
  expiry: DateTime,     // 5 minutes
  attempts: Number,     // max 3
  createdAt: DateTime
}
```

---

## 🔒 Security Features

<div align="center">

| Feature | Implementation | Protection |
|:---|:---|:---|
| 🔐 Password Storage | Bcrypt + Salt | Rainbow table attacks |
| 🎫 Session Token | JWT in HTTP-only cookie | XSS attacks |
| 🚫 Brute Force | 5 attempt limit + lock | Password guessing |
| ⏱️ OTP Expiry | 5 min + 3 attempts | Unauthorized reset |
| 🌐 CORS | Configured origins | Cross-origin attacks |
| ✅ Input Validation | Regex + sanitization | Injection attacks |

</div>

---

## 🛣️ Roadmap

<div align="center">

| Status | Feature |
|:---:|:---|
| ✅ | Authentication System |
| ✅ | Token Wallet |
| ✅ | User Dashboard |
| 🚧 | Content Marketplace |
| 📋 | Live Video Sessions |
| 📋 | AI Skill Matching |
| 📋 | Reputation System |
| 📋 | Mobile App |

</div>

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

```bash
# 1️⃣ Fork the repository

# 2️⃣ Create your feature branch
git checkout -b feature/AmazingFeature

# 3️⃣ Commit your changes
git commit -m '✨ Add AmazingFeature'

# 4️⃣ Push to the branch
git push origin feature/AmazingFeature

# 5️⃣ Open a Pull Request
```

---

## 👨‍💻 Author

<div align="center">

**Dilip Ravichandra**

[![Email](https://img.shields.io/badge/Email-diliprbtech24%40rvu.edu.in-red?style=for-the-badge&logo=gmail)](mailto:diliprbtech24@rvu.edu.in)
[![GitHub](https://img.shields.io/badge/GitHub-dilip--ravichandra-black?style=for-the-badge&logo=github)](https://github.com/dilip-ravichandra)

*Built with ❤️ at RV University*

**Agile PBL Project — 2026**

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

### ⭐ If you found this helpful, please star the repository!

<br/>

**[⬆ Back to Top](#-nexus)**

</div>

// ===========================
// UTILITY FUNCTIONS
// ===========================

function showNotification(message, type = 'info') {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = `notification ${type}`;
    notification.style.display = 'block';
    
    setTimeout(() => {
        notification.style.display = 'none';
    }, 4000);
}

function isValidEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(email);
}

function isValidPassword(password) {
    // Min 8 chars, 1 uppercase, 1 lowercase, 1 number
    if (password.length < 8) return false;
    if (!/[A-Z]/.test(password)) return false;
    if (!/[a-z]/.test(password)) return false;
    if (!/[0-9]/.test(password)) return false;
    return true;
}

// ===========================
// LOGIN FUNCTIONALITY
// ===========================

const loginForm = document.getElementById('loginForm');
if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value;
        
        // Validation
        if (!email || !password) {
            showNotification('Please fill in all fields', 'error');
            return;
        }
        
        if (!isValidEmail(email)) {
            showNotification('Please enter a valid email', 'error');
            return;
        }
        
        try {
            const response = await fetch('/api/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify({ email, password })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                showNotification('Login successful! Redirecting...', 'success');
                setTimeout(() => {
                    window.location.href = '/home.html';
                }, 1000);
            } else {
                showNotification(data.error || 'Login failed', 'error');
            }
        } catch (error) {
            showNotification('Network error. Please try again.', 'error');
        }
    });
}

// ===========================
// SIGNUP FUNCTIONALITY
// ===========================

const signupForm = document.getElementById('signupForm');
if (signupForm) {
    const teachingComfort = document.getElementById('teachingComfort');
    const teachingLevelGroup = document.getElementById('teachingLevelGroup');
    
    // Show/hide teaching level based on teaching comfort
    teachingComfort.addEventListener('change', (e) => {
        if (e.target.value === 'YES') {
            teachingLevelGroup.style.display = 'block';
            document.getElementById('teachingLevel').required = true;
        } else {
            teachingLevelGroup.style.display = 'none';
            document.getElementById('teachingLevel').required = false;
            document.getElementById('teachingLevel').value = '';
        }
    });
    
    signupForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = {
            fullName: document.getElementById('fullName').value.trim(),
            email: document.getElementById('email').value.trim(),
            password: document.getElementById('password').value,
            phoneNumber: document.getElementById('phoneNumber').value.trim(),
            university: document.getElementById('university').value.trim(),
            skillsKnown: document.getElementById('skillsKnown').value.trim(),
            skillsToImprove: document.getElementById('skillsToImprove').value.trim(),
            teachingComfort: document.getElementById('teachingComfort').value,
            teachingLevel: document.getElementById('teachingLevel').value
        };
        
        // Validation
        if (!formData.fullName || !formData.email || !formData.password || 
            !formData.phoneNumber || !formData.university || !formData.skillsKnown || 
            !formData.skillsToImprove || !formData.teachingComfort) {
            showNotification('Please fill in all required fields', 'error');
            return;
        }
        
        if (!isValidEmail(formData.email)) {
            showNotification('Please enter a valid email', 'error');
            return;
        }
        
        if (!isValidPassword(formData.password)) {
            showNotification('Password must be at least 8 characters with uppercase, lowercase, and number', 'error');
            return;
        }
        
        if (formData.teachingComfort === 'YES' && !formData.teachingLevel) {
            showNotification('Please select your teaching level', 'error');
            return;
        }
        
        try {
            const response = await fetch('/api/auth/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            if (response.ok) {
                showNotification('Signup successful! Redirecting to login...', 'success');
                setTimeout(() => {
                    window.location.href = '/login.html';
                }, 1500);
            } else {
                showNotification(data.error || 'Signup failed', 'error');
            }
        } catch (error) {
            showNotification('Network error. Please try again.', 'error');
        }
    });
}

// ===========================
// FORGOT PASSWORD MODAL
// ===========================

const forgotPasswordLink = document.getElementById('forgotPasswordLink');
const forgotPasswordModal = document.getElementById('forgotPasswordModal');
const closeModal = document.querySelector('.close');
const sendOtpBtn = document.getElementById('sendOtpBtn');
const resetPasswordBtn = document.getElementById('resetPasswordBtn');
const emailStep = document.getElementById('emailStep');
const otpStep = document.getElementById('otpStep');

if (forgotPasswordLink) {
    forgotPasswordLink.addEventListener('click', (e) => {
        e.preventDefault();
        forgotPasswordModal.style.display = 'block';
        emailStep.style.display = 'block';
        otpStep.style.display = 'none';
    });
}

if (closeModal) {
    closeModal.addEventListener('click', () => {
        forgotPasswordModal.style.display = 'none';
    });
}

window.addEventListener('click', (e) => {
    if (e.target === forgotPasswordModal) {
        forgotPasswordModal.style.display = 'none';
    }
});

// Send OTP
if (sendOtpBtn) {
    sendOtpBtn.addEventListener('click', async () => {
        const email = document.getElementById('resetEmail').value.trim();
        
        if (!email) {
            showNotification('Please enter your email', 'error');
            return;
        }
        
        if (!isValidEmail(email)) {
            showNotification('Please enter a valid email', 'error');
            return;
        }
        
        try {
            const response = await fetch('/api/auth/forgot-password', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                showNotification('OTP sent to your email!', 'success');
                emailStep.style.display = 'none';
                otpStep.style.display = 'block';
            } else {
                showNotification(data.error || 'Failed to send OTP', 'error');
            }
        } catch (error) {
            showNotification('Network error. Please try again.', 'error');
        }
    });
}

// Reset Password
if (resetPasswordBtn) {
    resetPasswordBtn.addEventListener('click', async () => {
        const email = document.getElementById('resetEmail').value.trim();
        const otp = document.getElementById('otp').value.trim();
        const newPassword = document.getElementById('newPassword').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        
        // Validation
        if (!otp || !newPassword || !confirmPassword) {
            showNotification('Please fill in all fields', 'error');
            return;
        }
        
        if (otp.length !== 6) {
            showNotification('OTP must be 6 digits', 'error');
            return;
        }
        
        if (newPassword !== confirmPassword) {
            showNotification('Passwords do not match', 'error');
            return;
        }
        
        if (!isValidPassword(newPassword)) {
            showNotification('Password must be at least 8 characters with uppercase, lowercase, and number', 'error');
            return;
        }
        
        try {
            const response = await fetch('/api/auth/reset-password', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, otp, newPassword })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                showNotification('Password reset successful! Redirecting to login...', 'success');
                forgotPasswordModal.style.display = 'none';
                setTimeout(() => {
                    window.location.href = '/login.html';
                }, 1500);
            } else {
                showNotification(data.error || 'Failed to reset password', 'error');
            }
        } catch (error) {
            showNotification('Network error. Please try again.', 'error');
        }
    });
}

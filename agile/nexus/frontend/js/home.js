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

// ===========================
// AUTHENTICATION CHECK
// ===========================

async function checkAuth() {
    try {
        const response = await fetch('/api/user/profile', {
            method: 'GET',
            credentials: 'include'
        });
        
        if (!response.ok) {
            // Not authenticated, redirect to login
            window.location.href = '/login.html';
            return null;
        }
        
        const data = await response.json();
        return data.user;
    } catch (error) {
        window.location.href = '/login.html';
        return null;
    }
}

// ===========================
// LOAD USER DATA
// ===========================

async function loadUserData() {
    const user = await checkAuth();
    
    if (!user) return;
    
    // Update username displays
    document.getElementById('usernameDisplay').textContent = user.fullName;
    document.getElementById('welcomeName').textContent = user.fullName;
    
    // Update token balance
    document.getElementById('tokenBalance').textContent = user.tokens;
    
    // Update skills known
    const skillsKnownContainer = document.getElementById('skillsKnown');
    if (user.skillsKnown && user.skillsKnown.length > 0) {
        skillsKnownContainer.innerHTML = user.skillsKnown
            .map(skill => `<span class="skill-tag">${skill}</span>`)
            .join('');
    } else {
        skillsKnownContainer.innerHTML = '<p style="color: #999;">No skills added yet</p>';
    }
    
    // Update skills to improve
    const skillsToImproveContainer = document.getElementById('skillsToImprove');
    if (user.skillsToImprove && user.skillsToImprove.length > 0) {
        skillsToImproveContainer.innerHTML = user.skillsToImprove
            .map(skill => `<span class="skill-tag">${skill}</span>`)
            .join('');
    } else {
        skillsToImproveContainer.innerHTML = '<p style="color: #999;">No skills added yet</p>';
    }
}

// ===========================
// LOGOUT FUNCTIONALITY
// ===========================

const logoutBtn = document.getElementById('logoutBtn');
if (logoutBtn) {
    logoutBtn.addEventListener('click', async () => {
        try {
            const response = await fetch('/api/auth/logout', {
                method: 'POST',
                credentials: 'include'
            });
            
            if (response.ok) {
                showNotification('Logged out successfully', 'success');
                setTimeout(() => {
                    window.location.href = '/login.html';
                }, 1000);
            } else {
                showNotification('Logout failed', 'error');
            }
        } catch (error) {
            showNotification('Network error', 'error');
        }
    });
}

// ===========================
// PROFILE TAB
// ===========================

const profileTab = document.getElementById('profileTab');
if (profileTab) {
    profileTab.addEventListener('click', async (e) => {
        e.preventDefault();
        const user = await checkAuth();
        if (user) {
            alert(`Profile Information:\n\nName: ${user.fullName}\nEmail: ${user.email}\nPhone: ${user.phoneNumber}\nUniversity: ${user.university}\nTeaching Comfort: ${user.teachingComfort}\nTeaching Level: ${user.teachingLevel || 'N/A'}`);
        }
    });
}

// ===========================
// TEACH TAB
// ===========================

const teachTab = document.getElementById('teachTab');
if (teachTab) {
    teachTab.addEventListener('click', (e) => {
        e.preventDefault();
        showNotification('Teaching feature coming soon!', 'info');
    });
}

// ===========================
// INITIALIZE
// ===========================

document.addEventListener('DOMContentLoaded', () => {
    loadUserData();
});

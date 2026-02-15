import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config

def send_otp_email(recipient_email, otp):
    """Send OTP email to user"""
    try:
        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = "NEXUS - Password Reset OTP"
        message["From"] = Config.EMAIL_USER
        message["To"] = recipient_email
        
        # Email body
        html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
                <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                    <h1 style="color: #667eea; text-align: center;">NEXUS</h1>
                    <h2 style="color: #333;">Password Reset Request</h2>
                    <p style="color: #666; font-size: 16px;">
                        You have requested to reset your password. Use the OTP below to complete the process:
                    </p>
                    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 5px; text-align: center; margin: 20px 0;">
                        <h1 style="color: #667eea; font-size: 36px; letter-spacing: 5px; margin: 0;">
                            {otp}
                        </h1>
                    </div>
                    <p style="color: #666; font-size: 14px;">
                        This OTP is valid for {Config.OTP_EXPIRY_MINUTES} minutes and can be used up to {Config.MAX_OTP_ATTEMPTS} times.
                    </p>
                    <p style="color: #999; font-size: 12px; margin-top: 30px;">
                        If you did not request this password reset, please ignore this email.
                    </p>
                    <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
                    <p style="color: #999; font-size: 12px; text-align: center;">
                        © 2026 NEXUS - AI-Driven Knowledge Exchange Platform
                    </p>
                </div>
            </body>
        </html>
        """
        
        # Attach HTML content
        part = MIMEText(html, "html")
        message.attach(part)
        
        # Send email
        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
            server.starttls()
            server.login(Config.EMAIL_USER, Config.EMAIL_PASS)
            server.sendmail(Config.EMAIL_USER, recipient_email, message.as_string())
        
        return True
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

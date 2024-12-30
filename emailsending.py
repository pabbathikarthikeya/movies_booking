import smtplib
from email.message import EmailMessage
import os

def send_email(sender_email, sender_password, receiver_email, subject, message, attachment_path=None):
    try:
        if not sender_email or not receiver_email or not subject or not message:
            raise ValueError("Email, subject, and message content must not be empty.")
        
        # Create the email message
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.set_content(message)

        # Attach the file if provided
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, 'rb') as attachment:
                file_data = attachment.read()
                file_name = os.path.basename(attachment_path)
                msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)
        
        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        print(f"Email sent successfully to {receiver_email}")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed: Check your email or app password.")
    except smtplib.SMTPException as e:
        print("SMTP error occurred:", str(e))
    except FileNotFoundError:
        print(f"Attachment file not found: {attachment_path}")
    except Exception as e:
        print("Error sending email:", str(e))

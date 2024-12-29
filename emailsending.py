import smtplib

def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        if not sender_email or not receiver_email or not subject or not message:
            raise ValueError("Email, subject, and message content must not be empty.")
        
        text = f"Subject: {subject}\n\n{message}"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"Email sent successfully to {receiver_email}")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed: Check your email or app password.")
    except smtplib.SMTPException as e:
        print("SMTP error occurred:", str(e))
    except Exception as e:
        print("Error sending email:", str(e))

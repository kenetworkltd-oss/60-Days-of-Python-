# Email Sender 
import smtplib
from email.mime.text import MIMEText 

# --- CONFIGURATION ---
my_email = "kenetworkltd@gmail.com"
my_password = "Aifi jnkf brrk mxvy"  # <--- PASTE YOUR APP PASSWORD HERE

# List of people to email
thier_email = [
    "agboolakehinde167@gmail.com", 
    "agbokenlogistics@gmail.com", 
    "marydoeswilliams@gmail.com"
]

subject = "Monthly updates"
content_text = "Hello, This is to report what is ongoing in the sales and it environs"

print("The mail is sending...")

# --- SENDING ---
try:
    # 1. Open the connection
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        
        # 2. Login (This must be INDENTED because it's inside the 'with' block)
        print("Logging in...")
        server.login(my_email, my_password) 
        print("Login successful!")
        
        # 3. Start the loop (INDENTED again)
        for person in thier_email:
            
            # Create the email envelope
            msg = MIMEText(content_text)
            msg['Subject'] = subject
            msg['From'] = my_email
            msg['To'] = person
            
            # 4. Send the email (INDENTED inside the loop)
            try:
                server.sendmail(my_email, person, msg.as_string())
                print(f"✅ Email sent to: {person}")
            except Exception as e:
                print(f"❌ Error sending to {person}: {e}")

except Exception as main_error:
    print(f"CRITICAL ERROR (Check Password or Internet): {main_error}")

print("Done!")
from smtp_service import SMTPService
 

SMTP_SERVER = SMTP_PORT = EMAIL_USERNAME = EMAIL_PASSWORD = None

with open('.env') as f:
    for line in f:
        if line.startswith('SMTP_SERVER'):
            SMTP_SERVER = line.split('=')[1].strip()
        elif line.startswith('SMTP_PORT'):
            SMTP_PORT = int(line.split('=')[1].strip())
        elif line.startswith('EMAIL_USERNAME'):
            EMAIL_USERNAME = line.split('=')[1].strip()
        elif line.startswith('EMAIL_PASSWORD'):
            EMAIL_PASSWORD = line.split('=')[1].strip()

smtp = SMTPService(SMTP_SERVER, SMTP_PORT, EMAIL_USERNAME, EMAIL_PASSWORD,)
smtp.send_email("frednobre18@gmail.com", "Test Email", "This is a test email from the SMTP service(je test mon bot c'est Fred tkt).")
mail_counter()


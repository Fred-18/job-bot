""" Ouvrir une connexion SMTP et envoyer un email. """
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart    

class SMTPService:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
         

    def send_email(self, to_email, subject, body):
        # Créer un message multipart
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Ajouter le corps du message au format texte
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Ouvrir une connexion SMTP sécurisée (TLS)
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Sécuriser la connexion
                server.login(self.username, self.password)  # Se connecter au serveur SMTP
                server.send_message(msg)  # Envoyer l'email
                print("Email envoyé avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email: {e}")


import os, base64
from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Mailgun:
   def __init__(self, subject, text, email_adress=None):
      self.scope = ["https://www.googleapis.com/auth/gmail.send"]
      self.client_json = "credentials.json"
      self.email_adress = email_adress
      self.subject = subject
      self.text = text

   def get_user_creds(self):
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", self.scope)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.client_json, self.scope)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as f:
                f.write(creds.to_json())
        return creds
   def gmail_send_message(self):
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = self.get_user_creds()

    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content(self.text)

        message["To"] = self.email_adress
        message["From"] = "devm25058@gmail.com"
        message["Subject"] =  self.subject

    # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")
        send_message = None
    return send_message


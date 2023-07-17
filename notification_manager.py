from twilio.rest import Client
import os

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
Frictional_Number = os.environ.get("Frictional_Number")
My_Number = os.environ.get("My_Number")

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


    def send_sms(self, message):
        message = self.client.messages.create(
            body= message,
            from_= Frictional_Number,
            to= My_Number
        )
        print(message.sid)

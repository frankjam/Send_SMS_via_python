import config
from twilio.rest import Client

#auth credentials 
account_sid = config.TWILIO_ACCOUNT_SID
auth_token = config.TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

def send_sms():
    global client
    message = client.messages.create(
                                body='Hi there',
                                from_='< PHONE NUMBER provided by twilio >',
                                to='< PHONE NUMBER to recieve sms >'
                            )
    return message.sid


print(send_sms())    
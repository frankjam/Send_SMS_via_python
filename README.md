"# Send_SMS_via_python" 
A simple way to programmatically send text messages using python. 

Requirements 
1. A  [Twilio](https://www.twilio.com/referral/Wbapp6) account.           <em>\`Click on the Twilio name to create an account\`</em>
2. Python installed

## Step 1: Setting up 

Create a virtual environment
```
 py -m venv twilio_sms
 ```
Activate the environment
``` 
\twilio_sms\Scripts\activate.bat
```
Create a  [Twilio](https://www.twilio.com/referral/Wbapp6) account to get your `ACCOUNT SID`, `AUTH TOKEN` and `PHONE NUMBER`

<em>The `ACCOUNT SID`, `AUTH TOKEN` will be used to allow you to use Twilio services.<br/>
The `PHONE NUMBER` will be used to send SMS to numbers of your choice.<br/>
You will be given $15 for trial of which upon depletion you can upgrade. </em>

Install the needed Twilio modules 
```
pip install twilio
```

## Step 2 Create a `config.py` file 
```
TWILIO_ACCOUNT_SID = '<Fill with your account sid>'
TWILIO_AUTH_TOKEN = '<Fill with AUTH token>'
```


## Step 3 Create an `app.py` file
```
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
                                from_='< PHONE NUMBER provided by Twilio >',
                                to='< PHONE NUMBER to receive SMS >'
                            )
    return message.sid


print(send_sms())
```
## Step 4 Run the `app.py` file 
This will send a text message to the number provided.

![IMG_20211129_211052.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1638209853357/zVF9AH4r8.jpeg)

<p>
<em> To remove the ** Sent from your Twilio trial account  ** </em>  upgrade your Twilio account  
<br>
[The complete code](https://github.com/frankjam/Send_SMS_via_python) 
<br><br>
Reference: 
[Twilio Documentation](https://www.twilio.com/docs/quickstart)
</p>

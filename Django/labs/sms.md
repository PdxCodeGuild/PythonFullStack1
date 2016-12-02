# Practice: Simple SMS


Create a django application that sends SMS text messages using the Twilio Python API

Create a webpage with a form prompting the user for a phone number and a message body.

POST the users data to your django application and inside the view, read from the POST dictionary,
and send the message via the Twiio API.

https://www.twilio.com/docs/quickstart/python/sms

Respond to the browser with a success message and display it to the user.

Be sure to make a new virtualenv and git repository for your project.

Here are thw Twilio Keys:
```
Token: 1769e4656916ec050cdbe4e58d17e6c1
SID: AC86189c370a1fcca6c3dd11c2fa15ee04
```
Here is an example of a call to twilio.

```
from twilio.rest import TwilioRestClient


account_sid = "AC86189c370a1fcca6c3dd11c2fa15ee04"
auth_token = "1769e4656916ec050cdbe4e58d17e6c1"
client = TwilioRestClient(account_sid, auth_token)
number = []

#numbers = ['+18456331959','+19714099425', '+13606245615', '+15037063889', '+15037810745', '+19712371510', '+15037379611']
day_numbers = ['+18067860264','+19713209937', '+15039808649', '+15038884575', '+19724153532', '+19724156381']

for number in day_numbers:
    message = client.messages.create(to=number, from_="+14243512633", body="Look Up!")
    print("Sent to {}".format(number))

```

### Advanced

Handle any number of individual messages and phone numbers on the webpage.
Parse the response in the view, and send all messages to thier respective recipients.

### Super Advanced

Make a django "SMSMessage" Model, and keep a history of the messages sent.
Using built in Django Auth, allow uers to sign in and view a history of thier messaging.

import time
from sinchsms import SinchSMS
number = '+56953890064'
message = 'I love SMS!'

client = SinchSMS("ed7a15d4-0af0-4c2e-a5ff-ac0904b6aebc", "q4lmt6bL2E62HX4QD4dwwQ==")

print("Sending '%s' to %s" % (message, number))
response = client.send_message(number, message)
message_id = response['messageId']

response = client.check_status(message_id)
while response['status'] != 'Successful':
    print(response['status'])
    time.sleep(1)
    response = client.check_status(message_id)
print(response['status'])

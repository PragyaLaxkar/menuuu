#!/usr/bin/python3
print("Content-type: text/html")
print("\n")

import pywhatkit as kit 
print("Whatapp send successfully")

# Specify the phone number (with country code) and the message
phone_number = "+916377097964"
message = "Hello from Python!"

# Send the message instantly
kit.sendwhatmsg_instantly(phone_number, message)

print("Whatapp send successfully")
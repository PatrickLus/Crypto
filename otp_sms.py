import requests
import json

# Define your Infobip credentials
BASE_URL = "https://l356g5.api.infobip.com" # Use the correct base URL for your region
API_KEY = "71ee7db6ea9d556bbb48e5c424d0cc62-f42ae8a4-1f5a-4d8c-8ae9-d8d8e6583fc6" # Use your own API key

# Define the SMS endpoint and headers
SMS_ENDPOINT = f"{BASE_URL}/sms/2/text/advanced"
HEADERS = {
    "Authorization": f"App {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def send_sms(phone_number, message):
    payload = {
        "messages": [
            {
                "from": "InfoSMS",
                "destinations": [{"to": phone_number}],
                "text": message
            }
        ]
    }
    response = requests.post(SMS_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 200:
        print(f"Message sent successfully to {phone_number}")
        print(response.json())
    else:
        print(f"Failed to send message to {phone_number}")
        print(response.text)

def send_otp_via_sms(phone_number, otp):
    message = f"Your OTP is {otp}"
    send_sms(phone_number, message)

def send_encrypted_message_via_sms(phone_number, encrypted_message):
    message = f"Your encrypted message is: {encrypted_message}"
    send_sms(phone_number, message)

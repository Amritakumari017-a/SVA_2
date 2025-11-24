import requests
import json

API_KEY = "AIzaSyCit-fYOKK2aXuE6HKIKc9h2Myp2RW9DkM"  # Replace with your real key

url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"

payload = {
    "contents": [
        {
            "role": "user",
            "parts": [
                {"text": "Hey Gemini 2.5! Give me a short greeting message to test this API connection."}
            ]
        }
    ]
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print("Status Code:", response.status_code)
print("Response:")
print(response.text)

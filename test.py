import requests

data = {
    "action": "push",
    "sender": {"login": "Shreedhar"}
}

response = requests.post("http://localhost:5000/webhook", json=data)
print(response.text)

import requests
import json

url = "http://127.0.0.1:8000/api/token/"

payload = json.dumps({
  "username": "prueba",
  "password": "prueba"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

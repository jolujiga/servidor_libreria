import requests

url = "http://127.0.0.1:8000/libreria/Genero/"

payload={'genero': 'Romantico'}
files=[

]
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5MDAzMjU4LCJpYXQiOjE2MzkwMDI5NTgsImp0aSI6IjYxYTZmMmY3NjFmZTRhNDc5MGNmOWFkZjM5ODJjMWI0IiwidXNlcl9pZCI6MX0.77qtEkWD-qAWJX2cnoftvwZrhx2unKswvP_j2BOD6qY'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

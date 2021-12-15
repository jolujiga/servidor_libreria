import requests

url = "http://127.0.0.1:8000/libreria/Genero/"

payload={}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5MDAyOTQ3LCJpYXQiOjE2MzkwMDI2NDcsImp0aSI6ImZmNzI1ZDBlYmNmMjQwYzViODU2NjkzNmQ5ZDZjN2UzIiwidXNlcl9pZCI6MX0.-wRln83OmpakwD7epreeXp11wtbRj702CnLRJoqZADg'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

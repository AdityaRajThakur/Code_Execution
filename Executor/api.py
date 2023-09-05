import requests
import json
url = "https://judge0-ce.p.rapidapi.com/submissions"

querystring = {"base64_encoded":"true","fields":"*"}

payload = {
	"language_id": 71,
	"source_code":  """
	a = int(intput()) 
	b = int(intput()) 
	print(a + b) """ , 
	
	"stdin": "12 12"
}
payload = json.dumps(payload) 
headers = {
	"content-type": "application/json",
	"Content-Type": "application/json",
	"X-RapidAPI-Key": "db9e3cdc0amsh826140a7f2f82f3p1dd862jsn12c3bebf19cc",
	"X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())
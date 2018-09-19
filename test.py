import requests

resp = requests.post(
	'http://127.0.0.1:8000/post/',
	data={"name": "12", 'age': 12}
	,
	headers={
		'Content-Type': 'application/x-www-form-urlencoded'
	}
)

print(resp.__dict__)
print(resp.status_code)
print(resp.text)
# print(resp.json())

import requests
import pprint


token = 'f771e60ce4b86157486b1ce0808239a45d474407'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/icos/icos/', headers=headers)

pprint.pprint(response.json())

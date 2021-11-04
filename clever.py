import requests

url = "https://api.clever.com/v3.0/sections"

querystring = {"limit": "379"}

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer DEMO_TOKEN"
}

response = requests.request("GET", url, headers=headers, params=querystring)

sections = response.json()['data']

section_students = []

for section in sections:
    section_students.append(len(section['data']['students']))

print(round(sum(section_students)/len(section_students)))

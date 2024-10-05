import requests

url = "https://hackapi.hellozelf.com/api/v1/ai_comment/"



body  = {

}
token = "<token>"
headers = {
    "Content-Type": "application/json",
    "X-API-Key": "<api_key>"
}

response = requests.request("delete", url=url, headers=headers);

if response.status_code not in [201, 200]:
    print(response.text)
print(response.status_code, response.json())

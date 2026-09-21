from azure.identity import AzureCliCredential
import requests
import json

credential = AzureCliCredential()

token = credential.get_token(
    "https://graph.microsoft.com/.default"
)

headers = {
    "Authorization": f"Bearer {token.token}"
}

response = requests.get(
    "https://graph.microsoft.com/v1.0/me",
    headers=headers
)

print("Status:", response.status_code)
print(json.dumps(response.json(), indent=4))

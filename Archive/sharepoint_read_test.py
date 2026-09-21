from azure.identity import AzureCliCredential
import requests

credential = AzureCliCredential()

token = credential.get_token(
    "https://graph.microsoft.com/.default"
)

headers = {
    "Authorization": f"Bearer {token.token}"
}

response = requests.get(
    "https://graph.microsoft.com/v1.0/sites/fuedu.sharepoint.com:/sites/KyberTechHostingAB",
    headers=headers
)

print(response.status_code)
print(response.text)
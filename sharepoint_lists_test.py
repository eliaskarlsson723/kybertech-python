from azure.identity import AzureCliCredential
import requests

credential = AzureCliCredential()

token = credential.get_token(
    "https://graph.microsoft.com/.default"
)

headers = {
    "Authorization": f"Bearer {token.token}"
}

# Hämta information om SharePoint-siten
site_response = requests.get(
    "https://graph.microsoft.com/v1.0/sites/fuedu.sharepoint.com:/sites/KyberTechHostingAB",
    headers=headers
)

site = site_response.json()

site_id = site["id"]

print("Site ID:")
print(site_id)

# Hämta alla listor
lists_response = requests.get(
    f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists",
    headers=headers
)

print("Statuskod:", lists_response.status_code)
print(lists_response.text)
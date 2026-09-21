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

# Hämta SharePoint-siten
site_response = requests.get(
    "https://graph.microsoft.com/v1.0/sites/fuedu.sharepoint.com:/sites/KyberTechHostingAB",
    headers=headers
)

print("Site status:", site_response.status_code)

site = site_response.json()

site_id = site["id"]

print("\nSite ID:")
print(site_id)

# Hämta SharePoint-listor
lists_response = requests.get(
    f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists",
    headers=headers
)

print("\nLists status:", lists_response.status_code)

lists = lists_response.json()

print("\nFullständigt svar från Graph:")
print(json.dumps(lists, indent=4))
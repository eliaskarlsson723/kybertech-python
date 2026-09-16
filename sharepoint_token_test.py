from azure.identity import AzureCliCredential

credential = AzureCliCredential()

token = credential.get_token(
    "https://fuedu.sharepoint.com/.default"
)

print("SharePoint-token hämtad!")
print(token.token[:20])
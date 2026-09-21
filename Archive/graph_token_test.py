from azure.identity import AzureCliCredential

credential = AzureCliCredential()

token = credential.get_token(
    "https://graph.microsoft.com/.default"
)

print("Graph-token hämtad!")
print(token.token[:20])
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()

token = credential.get_token(
    "https://management.azure.com/.default"
)

print("Azure token hämtad!")
print(token.token[:20])
from azure.identity import AzureCliCredential
import base64
import json

credential = AzureCliCredential()

token = credential.get_token(
    "https://graph.microsoft.com/.default"
)

parts = token.token.split(".")

payload = parts[1]

payload += "=" * (-len(payload) % 4)

decoded = base64.urlsafe_b64decode(payload)

claims = json.loads(decoded)

print("Microsoft Graph scopes:")

scopes = claims.get("scp", "")

for scope in scopes.split():
    print("-", scope)
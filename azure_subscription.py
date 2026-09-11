from azure.identity import DefaultAzureCredential
import subprocess
import json

# Testa Azure-autentisering
credential = DefaultAzureCredential()

token = credential.get_token(
    "https://management.azure.com/.default"
)

print("Azure-token hämtad!")
print(token.token[:20])

# Hämta prenumerationsinformation
result = subprocess.run(
    [
        r"C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd",
        "account",
        "show",
        "--output",
        "json"
    ],
    capture_output=True,
    text=True
)

subscription = json.loads(result.stdout)

# Skriv till fil
with open("azure_subscription.json", "w") as file:
    json.dump(subscription, file, indent=4)

print("azure_subscription.json skapad")
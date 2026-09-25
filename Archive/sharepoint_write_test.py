import os
from datetime import datetime

import msal
import requests


client_id = os.getenv("KYBERTECH_CLIENT_ID")
tenant_id = os.getenv("KYBERTECH_TENANT_ID")

if not client_id:
    raise RuntimeError("KYBERTECH_CLIENT_ID saknas.")

if not tenant_id:
    raise RuntimeError("KYBERTECH_TENANT_ID saknas.")


authority = f"https://login.microsoftonline.com/{tenant_id}"

scopes = [
    "Sites.ReadWrite.All"
]


app = msal.PublicClientApplication(
    client_id=client_id,
    authority=authority
)


flow = app.initiate_device_flow(
    scopes=scopes
)

if "user_code" not in flow:
    raise RuntimeError(
        f"Device flow kunde inte startas: {flow}"
    )


print(flow["message"])


result = app.acquire_token_by_device_flow(
    flow
)


if "access_token" not in result:
    print("Autentiseringen misslyckades.")
    print(
        result.get(
            "error_description",
            "Okänt autentiseringsfel."
        )
    )
    raise SystemExit(1)


print("\nGraph-autentisering lyckades!")


headers = {
    "Authorization": f"Bearer {result['access_token']}",
    "Content-Type": "application/json"
}


# --------------------------------------------------
# ENDAST KyberTech-Python-Analysis
# --------------------------------------------------

site_id = (
    "fuedu.sharepoint.com,"
    "bd87b2c1-d875-471d-9204-c949def00f69,"
    "255abd19-dc3b-4f35-ae25-d73de636ee05"
)

list_id = "f5c6002c-b182-4785-a612-4fc1cd079ec6"


items_url = (
    f"https://graph.microsoft.com/v1.0/"
    f"sites/{site_id}/lists/{list_id}/items"
)

print ("\nKyberTech-Python-Analysis URL:", items_url)
# --------------------------------------------------
# TYDLIG TESTDATA
# --------------------------------------------------

test_data = {
    "fields": {
        "ResourceName": "Python Integration Test",
        "HealthStatus": "Test",
        "EnvironmentScore": 0,
        "AlertLevel": "Test",
        "RunningVMs": 0,
        "StoppedVMs": 0,
        "LastUpdated": datetime.now().isoformat(),
        "Recommendations": "Integration test"
    }
}


print("\nSkapar EN testpost i KyberTech-Python-Analysis...")


response = requests.post(
    items_url,
    headers=headers,
    json=test_data,
    timeout=30
)


print(
    "SharePoint write status:",
    response.status_code
)


if response.status_code == 201:

    created_item = response.json()

    print("Testpost skapades!")
    print(
        "List Item ID:",
        created_item.get("id")
    )

else:

    print("Testpost kunde inte skapas.")
    print(response.text)

    raise SystemExit(1)
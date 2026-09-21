import os

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
    "Sites.Read.All"
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
    "Authorization": f"Bearer {result['access_token']}"
}


response = requests.get(
    "https://graph.microsoft.com/v1.0/me",
    headers=headers,
    timeout=30
)


print("Graph /me status:", response.status_code)
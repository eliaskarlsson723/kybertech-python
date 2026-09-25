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


# --------------------------------------------------
# READ-ONLY TEST
# Alla Graph-anrop nedan använder endast GET.
# --------------------------------------------------

hostname = "fuedu.sharepoint.com"
site_path = "sites/KyberTechHostingAB"

site_url = (
    f"https://graph.microsoft.com/v1.0/sites/"
    f"{hostname}:/{site_path}"
)


site_response = requests.get(
    site_url,
    headers=headers,
    timeout=30
)


print(
    "\nSharePoint site status:",
    site_response.status_code
)


if site_response.status_code != 200:
    print(site_response.text)
    raise SystemExit(1)


site = site_response.json()
site_id = site["id"]

print("Site hittad:")
print(site.get("displayName"))
print("Site ID:")
print(site_id)


# --------------------------------------------------
# Hämta listor
# --------------------------------------------------

lists_url = (
    f"https://graph.microsoft.com/v1.0/"
    f"sites/{site_id}/lists"
)


lists_response = requests.get(
    lists_url,
    headers=headers,
    timeout=30
)


print(
    "\nListor status:",
    lists_response.status_code
)


if lists_response.status_code != 200:
    print(lists_response.text)
    raise SystemExit(1)


target_list = None

for sp_list in lists_response.json().get("value", []):

    print(
        "Lista:",
        sp_list.get("displayName")
    )

    if sp_list.get("displayName") == "KyberTech-Python-Analysis":
        target_list = sp_list


if not target_list:
    print(
        "\nKyberTech-Python-Analysis hittades inte."
    )
    raise SystemExit(1)


list_id = target_list["id"]

print(
    "\nKyberTech-Python-Analysis hittades!"
)

print(
    "List ID:",
    list_id
)


# --------------------------------------------------
# Läs kolumner
# --------------------------------------------------

columns_url = (
    f"https://graph.microsoft.com/v1.0/"
    f"sites/{site_id}/lists/{list_id}/columns"
)


columns_response = requests.get(
    columns_url,
    headers=headers,
    timeout=30
)


print(
    "\nKolumner status:",
    columns_response.status_code
)


if columns_response.status_code != 200:
    print(columns_response.text)
    raise SystemExit(1)


print("\nKolumner:")

for column in columns_response.json().get("value", []):

    print(
        f"Display name: {column.get('displayName')} "
        f"| Internal name: {column.get('name')}"
    )
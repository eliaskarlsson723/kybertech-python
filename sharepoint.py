import os

import msal
import requests


SITE_ID = (
    "fuedu.sharepoint.com,"
    "bd87b2c1-d875-471d-9204-c949def00f69,"
    "255abd19-dc3b-4f35-ae25-d73de636ee05"
)

LIST_ID = "f5c6002c-b182-4785-a612-4fc1cd079ec6"


def write_analysis_to_sharepoint(analysis_data):

    client_id = os.getenv("KYBERTECH_CLIENT_ID")
    tenant_id = os.getenv("KYBERTECH_TENANT_ID")

    if not client_id:
        raise RuntimeError(
            "KYBERTECH_CLIENT_ID saknas."
        )

    if not tenant_id:
        raise RuntimeError(
            "KYBERTECH_TENANT_ID saknas."
        )

    authority = (
        f"https://login.microsoftonline.com/{tenant_id}"
    )

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
        raise RuntimeError(
            result.get(
                "error_description",
                "Graph-autentisering misslyckades."
            )
        )

    print("\nGraph-autentisering lyckades!")

    headers = {
        "Authorization": (
            f"Bearer {result['access_token']}"
        ),
        "Content-Type": "application/json"
    }

    items_url = (
        "https://graph.microsoft.com/v1.0/"
        f"sites/{SITE_ID}/lists/{LIST_ID}/items"
    )

    recommendations_text = "\n".join(
        analysis_data["recommendations"]
    )

    payload = {
        "fields": {
            "ResourceName": "KyberTech Azure Environment",
            "HealthStatus": analysis_data[
                "health_status"
            ],
            "EnvironmentScore": analysis_data[
                "environment_score"
            ],
            "AlertLevel": analysis_data[
                "alert_level"
            ],
            "RunningVMs": analysis_data[
                "running_vms"
            ],
            "StoppedVMs": analysis_data[
                "stopped_vms"
            ],
            "LastUpdated": analysis_data[
                "last_updated"
            ],
            "Recommendations": recommendations_text
        }
    }

    print(
        "\nSkickar analys till "
        "KyberTech-Python-Analysis..."
    )

    response = requests.post(
        items_url,
        headers=headers,
        json=payload,
        timeout=30
    )

    print(
        "SharePoint write status:",
        response.status_code
    )

    if response.status_code == 201:

        created_item = response.json()

        print("Analys skickad till SharePoint!")
        print(
            "List Item ID:",
            created_item.get("id")
        )

    else:

        print(
            "Analysen kunde inte skickas "
            "till SharePoint."
        )

        print(response.text)

        raise RuntimeError(
            "SharePoint-skrivningen misslyckades."
        )
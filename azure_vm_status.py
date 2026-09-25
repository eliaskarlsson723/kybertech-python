from analysis import analyze_environment
from sharepoint import write_analysis_to_sharepoint

import json
import os

from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient

from datetime import datetime

from azure.core.exceptions import (
    AzureError,
    ClientAuthenticationError,
    ResourceNotFoundError,
    ServiceRequestError
)

resource_group = "KyberTech-Resources"

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")

if not subscription_id:
    print(
        "Fel: AZURE_SUBSCRIPTION_ID saknas."
    )
    print(
        "Kontrollera programmets Azure-konfiguration."
    )
    raise SystemExit(1)

credential = AzureCliCredential()

compute_client = ComputeManagementClient(
    credential=credential,
    subscription_id=subscription_id
)

try:
    vms = list(
        compute_client.virtual_machines.list(
            resource_group
        )
    )

except ClientAuthenticationError:
    print(
        "Fel: Kunde inte autentisera mot Azure."
    )
    print(
        "Kontrollera att du är inloggad i Azure CLI."
    )
    raise SystemExit(1)

except ResourceNotFoundError:
    print(
        f"Fel: Resource Group '{resource_group}' kunde inte hittas."
    )
    raise SystemExit(1)

except ServiceRequestError:
    print(
        "Fel: Kunde inte ansluta till Azure."
    )
    print(
        "Kontrollera nätverksanslutningen."
    )
    raise SystemExit(1)

except AzureError as error:
    print(
        "Fel: Azure kunde inte hämta VM-information."
    )
    print(
        f"Detaljer: {error}"
    )
    raise SystemExit(1)

if not vms:
    print(
        f"Inga virtuella maskiner hittades i '{resource_group}'."
    )
    raise SystemExit(0)

resources = []

for vm in vms:

    try:
        instance_view = (
            compute_client.virtual_machines.instance_view(
                resource_group,
                vm.name
            )
        )

    except AzureError as error:
        print(
            f"Varning: Kunde inte läsa status för {vm.name}."
        )
        print(
            f"Detaljer: {error}"
        )

        instance_view = None

    status = "Unknown"

    if instance_view:

        for vm_status in instance_view.statuses:

            if vm_status.code == "PowerState/running":
                status = "Running"

            elif vm_status.code in (
                "PowerState/deallocated",
                "PowerState/stopped"
            ):
                status = "Stopped"

    device_type = "Unknown"

    if vm.tags:
        device_type = vm.tags.get(
            "DeviceType",
            "Unknown"
        )

    resources.append(
        {
            "name": vm.name,
            "status": status,
            "location": vm.location,
            "device_type": device_type,
            "cost": 0
        }
    )

analysis = analyze_environment(resources)

running = analysis["running_vms"]
stopped = analysis["stopped_vms"]

environment_score = analysis["environment_score"]
health_status = analysis["health_status"]
alert_level = analysis["alert_level"]
recommendations = analysis["recommendations"]

vm_details = []

for vm in resources:
    vm_details.append(
        {
            "name": vm["name"],
            "status": vm["status"],
            "location": vm["location"],
            "device_type": vm["device_type"]
        }
    )

critical_resources = []

for vm in resources:

    if vm["status"] == "Stopped":
        critical_resources.append(
            vm["name"]
        )

last_updated = datetime.now().astimezone().isoformat()

environment_summary = (
    f"Health Status: {health_status} | "
    f"Environment Score: {environment_score} | "
    f"Running VMs: {running} | "
    f"Stopped VMs: {stopped}"
)

dashboard = {
    "health_status": health_status,
    "environment_score": environment_score,
    "alert_level": alert_level,
    "last_updated": last_updated,
    "running_vms": running,
    "stopped_vms": stopped
}

actions = {
    "recommendations": recommendations,
    "critical_resources": critical_resources
}

inventory = {
    "vm_details": vm_details
}

summary = {
    "dashboard": dashboard,
    "actions": actions,
    "inventory": inventory,
    "environment_summary": environment_summary
}

sharepoint_payload = {
    "health_status": health_status,
    "environment_score": environment_score,
    "alert_level": alert_level,
    "running_vms": running,
    "stopped_vms": stopped,
    "last_updated": last_updated,
    "recommendations": recommendations
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)


with open("sharepoint_payload.json", "w") as file:
    json.dump(
        sharepoint_payload,
        file,
        indent=4
    )

write_analysis_to_sharepoint(
    sharepoint_payload
)

print(resources)
print(summary)
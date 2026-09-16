import subprocess
import json

from datetime import datetime

resource_group = "KyberTech-Resources"

result = subprocess.run(
    [
        r"C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd",
        "vm",
        "list",
        "-g",
        resource_group,
        "-d",
        "--output",
        "json"
    ],
    capture_output=True,
    text=True
)

vms = json.loads(result.stdout)

resources = []

for vm in vms:

    status = "Unknown"

    if vm["powerState"] == "VM running":
        status = "Running"

    elif vm["powerState"] == "VM deallocated":
        status = "Stopped"

    device_type = "Unknown"

    if "tags" in vm:
        device_type = vm["tags"].get(
            "DeviceType",
            "Unknown"
        )

    resources.append(
        {
            "name": vm["name"],
            "status": status,
            "location": vm["location"],
            "device_type": device_type,
            "cost": 0
        }
    )

running = 0
stopped = 0

stopped_vm_list = []

for vm in resources:

    if vm["status"] == "Running":
        running += 1

    if vm["status"] == "Stopped":
        stopped += 1
        stopped_vm_list.append(vm["name"])

if stopped > 0:
    health_status = "Warning"
else:
    health_status = "Healthy"

environment_score = int(
    (running / len(resources)) * 100
)

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

recommendations = []

if stopped > 0:
    recommendations.append(
        f"Review {stopped} stopped VMs"
    )

last_updated = datetime.now().strftime(
    "%Y-%m-%d %H:%M"
)

if running == len(resources):
    alert_level = "Green"

elif running == 0:
    alert_level = "Red"

else:
    alert_level = "Yellow"

environment_status = {
    "health_status": health_status,
    "environment_score": environment_score,
    "running_vms": running,
    "stopped_vms": stopped,
    "last_updated": last_updated,
    "alert_level": alert_level
}

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


print(resources)
print(summary)
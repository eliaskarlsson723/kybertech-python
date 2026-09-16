import subprocess
import json

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

environment_score = 100

if stopped > 0:
    environment_score -= 20

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

summary = {
    "total_vms": len(resources),
    "running_vms": running,
    "stopped_vms": stopped,
    "health_status": health_status,
    "environment_score": environment_score,
    "stopped_vm_list": stopped_vm_list,
    "vm_details": vm_details
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print(resources)
print(summary)
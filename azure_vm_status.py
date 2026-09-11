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

    resources.append(
        {
            "name": vm["name"],
            "status": status,
            "cost": 0
        }
    )

print(resources)
import json

with open("azure_vms.json", "r") as file:
    azure_vms = json.load(file)

resources = []

for vm in azure_vms:
    resources.append(
        {
            "name": vm["name"],
            "status": "Unknown",
            "cost": 0
        }
    )

    total_vms = len(resources)

summary = {
    "total_vms": total_vms
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print(summary)
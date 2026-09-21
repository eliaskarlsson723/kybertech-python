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

print(resources)

print("Antal Azure VM:", len(resources))
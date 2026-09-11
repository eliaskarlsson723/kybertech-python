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
        "--output",
        "json"
    ],
    capture_output=True,
    text=True
)

vms = json.loads(result.stdout)

with open("azure_vms.json", "w") as file:
    json.dump(vms, file, indent=4)

print("azure_vms.json skapad")
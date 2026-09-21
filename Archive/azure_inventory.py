import subprocess

resource_group = "KyberTech-Resources"

result = subprocess.run(
    [
        r"C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd",
        "vm",
        "list",
        "-g",
        resource_group,
        "--output",
        "table"
    ],
    capture_output=True,
    text=True
)

print(result.stdout)
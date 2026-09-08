import json

with open("resources.json", "r") as file:
    resources = json.load(file)

for vm in resources:
    print(vm["name"], "-", vm["status"], "-", vm["cost"], "kr")

running = 0
stopped = 0
total_cost = 0

for vm in resources:
    if vm["status"] == "Running":
        running += 1
    if vm ["status"] == "Stopped":
        stopped += 1
    total_cost += vm["cost"]

print("Antal VM som är igång:", running)
print("Antal VM som är stoppade:", stopped)
print("Total kostnad:", total_cost, "kr")

average_cost = total_cost / len(resources)

print("Genomsnittlig kostnad per VM:", average_cost, "kr")

most_expensive = resources[0]

for vm in resources:
    if vm["cost"] > most_expensive["cost"]:
        most_expensive = vm

print("Dyraste VM:")
print(most_expensive["name"], "-", most_expensive["cost"], "kr")

summary = {
    "running_vms": running,
    "stopped_vms": stopped,
    "total_cost": total_cost,
    "average_cost": average_cost,
    "most_expensive_vm": most_expensive["name"]
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)
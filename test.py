import json

with open("resources.json", "r") as file:
    resources = json.load(file)

for vm in resources:
    print(vm["name"], "-", vm["status"], "-", vm["cost"], "kr")

running = 0
stopped = 0
total_cost = 0

running_cost = 0
stopped_cost = 0

for vm in resources:
    if vm["status"] == "Running":
        running += 1
        running_cost += vm["cost"]
    if vm ["status"] == "Stopped":
        stopped += 1
        stopped_cost += vm["cost"]
    total_cost += vm["cost"]

print("Antal VM som är igång:", running)
print("Antal VM som är stoppade:", stopped)
print("Total kostnad:", total_cost, "kr")
print("Total kostnad för Running VM:", running_cost, "kr")
print("Total kostnad för Stopped VM:", stopped_cost, "kr")

average_cost = total_cost / len(resources)

print("Genomsnittlig kostnad per VM:", average_cost, "kr")

if stopped > 0:
    health_status = "Warning"
else:
    health_status = "Healthy"

most_expensive = resources[0]

for vm in resources:
    if vm["cost"] > most_expensive["cost"]:
        most_expensive = vm

print("Dyraste VM:")
print(most_expensive["name"], "-", most_expensive["cost"], "kr")

print("VM med hög kostnad:")

high_cost_vms = []

for vm in resources:
    if vm["cost"] > 1000:
        high_cost_vms.append(vm["name"])
        print("-", vm["name"], "-", vm["cost"], "kr")

print("Miljöstatus:", health_status)

summary = {
    "running_vms": running,
    "stopped_vms": stopped,
    "running_cost": running_cost,
    "stopped_cost": stopped_cost,
    "total_cost": total_cost,
    "average_cost": average_cost,
    "most_expensive_vm": most_expensive["name"],
    "high_cost_vms": high_cost_vms,
    "health_status": health_status
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)
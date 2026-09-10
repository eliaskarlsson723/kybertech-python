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

environment_score = 100

stopped_vm_list = []

for vm in resources:
    if vm["status"] == "Running":
        running += 1
        running_cost += vm["cost"]
    if vm ["status"] == "Stopped":
        stopped += 1
        stopped_cost += vm["cost"]
        stopped_vm_list.append(vm["name"])
    total_cost += vm["cost"]

print("Antal VM som är igång:", running)
print("Antal VM som är stoppade:", stopped)
print("Total kostnad:", total_cost, "kr")
print("Total kostnad för Running VM:", running_cost, "kr")
print("Total kostnad för Stopped VM:", stopped_cost, "kr")

average_cost = total_cost / len(resources)

print("Genomsnittlig kostnad per VM:", average_cost, "kr")

if stopped > 0:
    environment_score -= 20
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

environment_score -= len(high_cost_vms) * 10

print("Miljöstatus:", health_status)

print("Environment Score:", environment_score)

potential_savings = stopped_cost

print("Potentiell besparing:", potential_savings, "kr")

recommendations = []

if stopped > 0:
    recommendations.append(
        f"Review {stopped} stopped VMs"
    )

if len(high_cost_vms) > 0:
    recommendations.append(
        f"Investigate {len(high_cost_vms)} high-cost VMs"
    )

    print("Recommendations:")

for recommendation in recommendations:
    print("-", recommendation)

print("Stopped VM List:")
for vm_name in stopped_vm_list:
    print("-", vm_name)


summary = {
    "running_vms": running,
    "stopped_vms": stopped,
    "stopped_vm_list": stopped_vm_list,
    "running_cost": running_cost,
    "stopped_cost": stopped_cost,
    "total_cost": total_cost,
    "average_cost": average_cost,
    "most_expensive_vm": most_expensive["name"],
    "high_cost_vms": high_cost_vms,
    "health_status": health_status,
    "environment_score": environment_score,
    "potential_savings": potential_savings,
    "recommendations": recommendations
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)

for vm in resources:

    if "name" not in vm:
        print("Fel: En VM saknar namn")

    if "status" not in vm:
        print("Fel: En VM saknar status")

    if "cost" not in vm:
        print("Fel: En VM saknar kostnad")

    elif vm["cost"] < 0:
        print("Fel: Negativ kostnad upptäckt:", vm["name"])
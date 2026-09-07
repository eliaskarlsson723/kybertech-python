import json

with open("resources.json", "r") as file:
    resources = json.load(file)

for vm in resources:
    print(vm["name"], "-", vm["status"], "-", vm["cost"], "kr")

running = 0
total_cost = 0

for vm in resources:
    if vm["status"] == "Running":
        running += 1

    total_cost += vm["cost"]

print("Antal VM som är igång:", running)
print("Total kostnad:", total_cost, "kr")

most_expensive = resources[0]

for vm in resources:
    if vm["cost"] > most_expensive["cost"]:
        most_expensive = vm

print("Dyraste VM:")
print(most_expensive["name"], "-", most_expensive["cost"], "kr")
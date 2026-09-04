resources = [
    {"name": "VM-01", "status": "Running", "cost": 1200},
    {"name": "VM-02", "status": "Stopped", "cost": 800},
    {"name": "VM-03", "status": "Running", "cost": 1500}
]

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
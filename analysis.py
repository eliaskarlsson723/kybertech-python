def analyze_environment(resources):
    total_vms = len(resources)

    running = sum(
        1
        for vm in resources
        if vm["status"] == "Running"
    )

    stopped = sum(
        1
        for vm in resources
        if vm["status"] == "Stopped"
    )

    if total_vms == 0:
        environment_score = 0
    else:
        environment_score = int(
            (running / total_vms) * 100
        )

    if running == total_vms and total_vms > 0:
        health_status = "Healthy"
        alert_level = "Green"

    elif running == 0:
        health_status = "Warning"
        alert_level = "Red"

    else:
        health_status = "Warning"
        alert_level = "Yellow"

    recommendations = []

    if stopped > 0:
        recommendations.append(
            f"Review {stopped} stopped VMs"
        )

    return {
        "health_status": health_status,
        "environment_score": environment_score,
        "alert_level": alert_level,
        "running_vms": running,
        "stopped_vms": stopped,
        "recommendations": recommendations
    }
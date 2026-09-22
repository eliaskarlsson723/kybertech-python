from analysis import analyze_environment


def test_all_vms_running():

    resources = [
        {"status": "Running"},
        {"status": "Running"}
    ]

    result = analyze_environment(resources)

    assert result["running_vms"] == 2
    assert result["stopped_vms"] == 0
    assert result["environment_score"] == 100
    assert result["health_status"] == "Healthy"
    assert result["alert_level"] == "Green"
    assert result["recommendations"] == []


def test_one_vm_stopped():

    resources = [
        {"status": "Running"},
        {"status": "Stopped"}
    ]

    result = analyze_environment(resources)

    assert result["running_vms"] == 1
    assert result["stopped_vms"] == 1
    assert result["environment_score"] == 50
    assert result["health_status"] == "Warning"
    assert result["alert_level"] == "Yellow"
    assert result["recommendations"] == [
        "Review 1 stopped VMs"
    ]


def test_all_vms_stopped():

    resources = [
        {"status": "Stopped"},
        {"status": "Stopped"}
    ]

    result = analyze_environment(resources)

    assert result["running_vms"] == 0
    assert result["stopped_vms"] == 2
    assert result["environment_score"] == 0
    assert result["health_status"] == "Warning"
    assert result["alert_level"] == "Red"
    assert result["recommendations"] == [
        "Review 2 stopped VMs"
    ]
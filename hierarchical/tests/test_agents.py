from agenttask import (
    manager,
    carpentry_specialist,
    plumbing_specialist,
    electrical_specialist,
)


def test_manager():
    assert manager.role == "Kitchen Support Manager"
    assert manager.allow_delegation is True
    assert manager.memory is not None


def test_carpentry_specialist():
    assert carpentry_specialist.role == "Cupboard Specialist"
    assert carpentry_specialist.memory is not None


def test_plumbing_specialist():
    assert plumbing_specialist.role == "Water Tap Specialist"
    assert plumbing_specialist.memory is not None


def test_electrical_specialist():
    assert electrical_specialist.role == "Electrical Appliance Specialist"
    assert electrical_specialist.memory is not None
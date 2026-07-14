from agenttask import kitchen_issue_task


def test_task_created():
    assert kitchen_issue_task is not None


def test_task_description():
    assert "Kitchen Support Manager" in kitchen_issue_task.description


def test_expected_output():
    assert "manager should provide" in kitchen_issue_task.expected_output.lower()
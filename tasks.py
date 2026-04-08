def easy_task(action, observation=None):
    if action.get("category"):
        return 0.9
    return 0.1


def medium_task(action, observation=None):
    if action.get("category") and action.get("department"):
        return 0.8
    return 0.4


def hard_task(action, observation=None):
    if (
        action.get("category")
        and action.get("department")
        and action.get("inspect")
        and action.get("assign_truck")
        and action.get("cleanup_complete")
    ):
        return 0.85
    return 0.45


# Explicit grader registry (important for validator)
GRADERS = {
    "easy": easy_task,
    "medium": medium_task,
    "hard": hard_task,
}
    else:
        score = 0.45
    return float(score)

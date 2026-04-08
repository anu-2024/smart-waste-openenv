def easy_task(action, observation=None):
    if action.get("category"):
        score = 0.9
    else:
        score = 0.1
    return float(score)


def medium_task(action, observation=None):
    if action.get("category") and action.get("department"):
        score = 0.8
    else:
        score = 0.4
    return float(score)


def hard_task(action, observation=None):
    if (
        action.get("category")
        and action.get("department")
        and action.get("inspect")
        and action.get("assign_truck")
        and action.get("cleanup_complete")
    ):
        score = 0.85
    else:
        score = 0.45
    return float(score)

def _to_dict(action):
    """Convert Action object or dict to dict"""
    if hasattr(action, "dict"):
        return action.dict()
    return action


def easy_task(action, observation=None):

    a = _to_dict(action)

    if a.get("category"):
        return 0.85
    return 0.15


def medium_task(action, observation=None):

    a = _to_dict(action)

    if a.get("category") and a.get("department"):
        return 0.80
    return 0.30


def hard_task(action, observation=None):

    a = _to_dict(action)

    if (
        a.get("category")
        and a.get("department")
        and a.get("inspect")
        and a.get("assign_truck")
        and a.get("cleanup_complete")
    ):
        return 0.90

    return 0.40


GRADERS = {
    "easy": easy_task,
    "medium": medium_task,
    "hard": hard_task,
}

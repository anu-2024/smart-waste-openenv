def _to_dict(action):
    try:
        if hasattr(action, "dict"):
            return action.dict()
        if hasattr(action, "__dict__"):
            return action.__dict__
        if isinstance(action, dict):
            return action
    except Exception:
        pass
    return {}


def easy_task(action, observation=None, info=None):
    a = _to_dict(action)

    if a.get("category"):
        return 0.6
    return 0.4


def medium_task(action, observation=None, info=None):
    a = _to_dict(action)

    if a.get("category") and a.get("department"):
        return 0.7
    return 0.3


def hard_task(action, observation=None, info=None):
    a = _to_dict(action)

    if a.get("department") == "sanitation_team":
        return 0.8
    return 0.2


GRADERS = {
    "easy": easy_task,
    "medium": medium_task,
    "hard": hard_task,
}

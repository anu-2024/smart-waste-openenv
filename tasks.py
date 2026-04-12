def clamp(v):
    try:
        v = float(v)
    except:
        v = 0.5

    if v <= 0:
        v = 0.01
    if v >= 1:
        v = 0.99

    return v


def easy_task(action, observation=None, info=None):
    score = 0.3

    if action.get("category"):
        score += 0.2

    if action.get("department"):
        score += 0.2

    return clamp(score)


def medium_task(action, observation=None, info=None):
    score = 0.2

    if action.get("category"):
        score += 0.2

    if action.get("department"):
        score += 0.2

    if action.get("inspect"):
        score += 0.2

    return clamp(score)


def hard_task(action, observation=None, info=None):
    score = 0.2

    if action.get("category"):
        score += 0.15

    if action.get("department"):
        score += 0.15

    if action.get("inspect"):
        score += 0.15

    if action.get("assign_truck"):
        score += 0.15

    if action.get("cleanup_complete"):
        score += 0.15

    return clamp(score)


GRADERS = {
    "easy": easy_task,
    "medium": medium_task,
    "hard": hard_task,
}

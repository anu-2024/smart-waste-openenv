def clamp(score):
    return max(0.01, min(0.99, float(score)))


def easy_task(action, observation=None, info=None):
    score = 0.2

    if action.get("category"):
        score += 0.3

    if action.get("department"):
        score += 0.3

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
        score += 0.2

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

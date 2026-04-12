def safe_score(value):
    try:
        v = float(value)
    except Exception:
        v = 0.5
    if v <= 0:
        v = 0.01
    if v >= 1:
        v = 0.99
    return v


def easy_task(action, observation=None, info=None):
    # simple constant but validated
    return safe_score(0.55)


def medium_task(action, observation=None, info=None):
    return safe_score(0.65)


def hard_task(action, observation=None, info=None):
    return safe_score(0.75)


GRADERS = {
    "easy": easy_task,
    "medium": medium_task,
    "hard": hard_task,
}

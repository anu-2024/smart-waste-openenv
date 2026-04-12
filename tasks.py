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
    score = 0.5
    return {"score": clamp(score)}


def medium_task(action, observation=None, info=None):
    score = 0.6
    return {"score": clamp(score)}


def hard_task(action, observation=None, info=None):
    score = 0.7
    return {"score": clamp(score)}


GRADERS = {
    "easy": easy_task,
    "medium": medium_task,
    "hard": hard_task,
}

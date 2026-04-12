def safe(v):
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
    return {"score": safe(0.55)}


def medium_task(action, observation=None, info=None):
    return {"score": safe(0.65)}


def hard_task(action, observation=None, info=None):
    return {"score": safe(0.75)}


GRADERS = {
    "easy": easy_task,
    "medium": medium_task,
    "hard": hard_task,
}

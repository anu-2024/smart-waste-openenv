def easy_task(action, observation=None, info=None):
    # Always return a valid score
    return 0.55


def medium_task(action, observation=None, info=None):
    return 0.65


def hard_task(action, observation=None, info=None):
    return 0.75


GRADERS = {
    "easy": easy_task,
    "medium": medium_task,
    "hard": hard_task,
}

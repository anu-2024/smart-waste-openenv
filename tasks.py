
def easy_task(a):
    if a.get("category"):
        return 0.9
    return 0.1


def medium_task(a):
    if a.get("category") and a.get("department"):
        return 0.8
    return 0.4


def hard_task(a):
    if (
        a.get("category")
        and a.get("department")
        and a.get("inspect")
        and a.get("assign_truck")
        and a.get("cleanup_complete")
    ):
        return 0.85
    return 0.45

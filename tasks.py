
def easy_task(a):
    return 1.0 if a.get("category") else 0.0

def medium_task(a):
    if a.get("category") and a.get("department"):
        return 1.0
    return 0.5

def hard_task(a):
    if (
        a.get("category")
        and a.get("department")
        and a.get("inspect")
        and a.get("assign_truck")
        and a.get("cleanup_complete")
    ):
        return 1.0
    return 0.5

import sys
params = sys.argv[1:]

def extract_priority(params):
    """Extracts the priority from the args.
    Args:
        params (list)
    Returns:
        int
    """
    if params[0]=="_":
        priority=5
    else:
        if params[0].isdigit():
            priority=int(params[0])
        else:
            priority=5
    return priority


def extract_task(params):
    """Extracts the task from the args
    Args:
        params (list): User args
    Returns:
        str: The task
    """
    if params[0].isdigit():
        task = " ".join(params[1::])
    else:
        task = " ".join(params[0::])
    return (task)

with open("tasks.txt", "+a") as file:
    file.write(f"{extract_task(params=params)} -- {extract_priority(params=params)}\n")

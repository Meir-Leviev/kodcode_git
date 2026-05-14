from tabulate import tabulate

# A list of dictionaries for the tasks
tasks = [
    {"task_name": "feed the dog", "priority": "medium", "is_done": False},
    {"task_name": "buy groceries", "priority": "high", "is_done": False},
    {"task_name": "water the plants", "priority": "low", "is_done": True},
    {"task_name": "pay electricity bill", "priority": "high", "is_done": False},
    {"task_name": "read a book", "priority": "low", "is_done": False},
]


def completion_convert(is_done) -> str:
    return "completed" if is_done else "not completed"


def print_tasks(tasks: list[dict]) -> None:
    tasks_copy = []
    for task in tasks:
        task["is_done"] = completion_convert(task["is_done"])
        tasks_copy.append(task)
    print(tabulate(tasks_copy))


def finished_tasks(tasks: list[dict]) -> int:
    finished_cnt = 0
    for task in tasks:
        is_done = task.get("is_done")
        if is_done:
            finished_cnt += 1
    return finished_cnt


def unfinished_tasks(tasks) -> int:
    return len(tasks) - finished_tasks(tasks)


def high_priority_tasks(tasks: list[dict]) -> int:
    cnt = 0
    for task in tasks:
        priority = task.get("priority")
        if priority == "high":
            cnt += 1
    return cnt


def print_daily_summery(tasks: list[dict]) -> None:
    total_tasks = len(tasks)
    open_tasks = unfinished_tasks(tasks)
    close_tasks = finished_tasks(tasks)
    urgent_tasks = high_priority_tasks(tasks)
    print()
    print("--- daily summery ---")
    print(f"total tasks: {total_tasks}")
    print(f"open tasks: {open_tasks}")
    print(f"close tasks: {close_tasks}")
    print(f"urgent tasks: {urgent_tasks}")


print_tasks(tasks)

print_daily_summery(tasks)

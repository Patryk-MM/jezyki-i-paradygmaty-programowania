def procedural_activity_selection(tasks):
    tasks.sort(key=lambda x: x[1])
    selected_tasks = []
    last_end_time = 0
    total_reward = 0

    for task in tasks:
        start, end, reward = task
        if start >= last_end_time:
            selected_tasks.append(task)
            last_end_time = end
            total_reward += reward

    return total_reward, selected_tasks


def functional_activity_selection(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[1])

    def select_tasks(remaining_tasks, last_end_time=0, selected_tasks=[], total_reward=0):
        if not remaining_tasks:
            return total_reward, selected_tasks

        first, *rest = remaining_tasks
        start, end, reward = first

        if start >= last_end_time:
            return select_tasks(rest, end, selected_tasks + [first], total_reward + reward)
        else:
            return select_tasks(rest, last_end_time, selected_tasks, total_reward)

    return select_tasks(sorted_tasks)


tasks = [
    (1, 3, 5),
    (2, 5, 6),
    (4, 6, 5),
    (6, 7, 4),
    (5, 8, 11),
    (8, 9, 2)
]

print("Proceduralne podejście:")
proc_reward, proc_selected = procedural_activity_selection(tasks)
print("Maksymalna nagroda:", proc_reward)
print("Wybrane zadania:", proc_selected)

print("\nFunkcyjne podejście:")
func_reward, func_selected = functional_activity_selection(tasks)
print("Maksymalna nagroda:", func_reward)
print("Wybrane zadania:", func_selected)

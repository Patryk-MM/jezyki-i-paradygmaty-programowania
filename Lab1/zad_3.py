from functools import reduce


def procedural_task_scheduling(tasks):
    tasks.sort(key=lambda x: x[1])

    total_waiting_time = 0
    waiting_time = 0
    optimal_order = []

    for task in tasks:
        optimal_order.append(task)
        total_waiting_time += waiting_time
        waiting_time += task[1]

    return optimal_order, total_waiting_time


def functional_task_scheduling(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[1])

    waiting_times = list(map(lambda i: sum(t[1] for t in sorted_tasks[:i]), range(len(sorted_tasks))))
    total_waiting_time = reduce(lambda acc, wt: acc + wt, waiting_times, 0)

    return sorted_tasks, total_waiting_time


tasks = [
    ("Zadanie A", 3, 10),
    ("Zadanie B", 1, 5),
    ("Zadanie C", 2, 8),
    ("Zadanie D", 5, 12)
]

print("Proceduralne podejście:")
proc_order, proc_time = procedural_task_scheduling(tasks[:])
print("Kolejność zadań:", proc_order)
print("Całkowity czas oczekiwania:", proc_time)

print("\nFunkcyjne podejście:")
func_order, func_time = functional_task_scheduling(tasks[:])
print("Kolejność zadań:", func_order)
print("Całkowity czas oczekiwania:", func_time)

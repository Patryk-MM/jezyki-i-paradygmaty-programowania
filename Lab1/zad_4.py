def procedural_knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(capacity + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][0]

    return dp[n][capacity], selected_items


def functional_knapsack(items, capacity):
    def knapsack_recursive(i, w):
        if i == 0 or w == 0:
            return 0, []

        weight, value = items[i - 1]
        if weight > w:
            return knapsack_recursive(i - 1, w)

        without_item = knapsack_recursive(i - 1, w)
        with_item = knapsack_recursive(i - 1, w - weight)
        with_item = (with_item[0] + value, with_item[1] + [items[i - 1]])

        return max(without_item, with_item, key=lambda x: x[0])

    return knapsack_recursive(len(items), capacity)


items = [
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 8)
]
capacity = 5

print("Proceduralne podejście:")
proc_value, proc_selected = procedural_knapsack(items, capacity)
print("Maksymalna wartość:", proc_value)
print("Wybrane przedmioty:", proc_selected)

print("\nFunkcyjne podejście:")
func_value, func_selected = functional_knapsack(items, capacity)
print("Maksymalna wartość:", func_value)
print("Wybrane przedmioty:", func_selected)
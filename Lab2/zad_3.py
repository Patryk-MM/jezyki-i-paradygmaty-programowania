def analyze_mixed_data(data):
    numeric_values = list(filter(lambda x: isinstance(x, (int, float)), data))
    string_values = list(filter(lambda x: isinstance(x, str), data))
    tuple_values = list(filter(lambda x: isinstance(x, tuple), data))

    max_number = max(numeric_values, default=None)
    longest_string = max(string_values, key=len, default=None)
    largest_tuple = max(tuple_values, key=len, default=None)

    return {
        "max_number": max_number,
        "longest_string": longest_string,
        "largest_tuple": largest_tuple
    }



data = [3, "hello", (1, 2, 3), 7.5, "world", (1, 2), 42, {"key": "value"}, "longest_string_here", (4, 5, 6, 7)]
result = analyze_mixed_data(data)
print(result)

import numpy as np
import re


def validate_and_execute(operation, matrices):
    try:
        if operation.startswith("add"):
            m1, m2 = re.findall(r'\d+', operation)
            m1, m2 = matrices[int(m1)], matrices[int(m2)]
            if m1.shape != m2.shape:
                return "Error: Matrices must have the same dimensions for addition."
            return m1 + m2

        elif operation.startswith("multiply"):
            m1, m2 = re.findall(r'\d+', operation)
            m1, m2 = matrices[int(m1)], matrices[int(m2)]
            if m1.shape[1] != m2.shape[0]:
                return "Error: Matrices must have compatible dimensions for multiplication."
            return np.dot(m1, m2)

        elif operation.startswith("transpose"):
            m = int(re.findall(r'\d+', operation)[0])
            return matrices[m].T

        else:
            return "Error: Unsupported operation."

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    matrices = [
        np.array([[1, 2], [3, 4]]),
        np.array([[5, 6], [7, 8]]),
        np.array([[1, 2, 3], [4, 5, 6]])
    ]

    operations = ["add 0 1", "multiply 0 1", "transpose 2"]

    for op in operations:
        result = validate_and_execute(op, matrices)
        print(f"Operation: {op}\nResult:\n{result}\n")

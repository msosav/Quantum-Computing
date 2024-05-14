import numpy as np


def oracle(elements, marked):
    """
    This function creates an oracle function.
    Args:
        elements (list): A list of elements.
        marked (list): A list of marked elements.
    Returns:
        (list): A list of -1 and 1.
    """
    return [(-1 if i in marked else 1) for i in elements]


def grovers_algorithm(elements, marked):
    """
    This function implements the Grover's algorithm.
    Args:
        elements (list): A list of elements.
        marked (list): A list of marked elements.
    Returns:
        (list): A list of probabilities.
    """
    n = len(elements)
    num_iterations = int(np.pi / 4 * np.sqrt(n))
    state = np.ones(n) / np.sqrt(n)

    oracle_matrix = np.diag(oracle(elements, marked))

    for _ in range(num_iterations):
        state = 2 * np.dot(oracle_matrix, state) - state
        state = state / np.linalg.norm(state)
        state = 2 * np.dot(oracle_matrix, state) - state

    return state


if __name__ == "__main__":
    print("Grovers Algorithm")
    print("---------------------------------------------------------")

    num_qubits = 3

    print("Numer of Qubits:", num_qubits)

    elements = [i for i in range(2 ** num_qubits)]

    marked = [0]

    probabilities = grovers_algorithm(elements, marked)

    print("---------------------------------------------------------")

    print("Probabilities:", probabilities)

    print("---------------------------------------------------------")

    print("Max Probability:", max(probabilities),
          "at index", np.argmax(probabilities))

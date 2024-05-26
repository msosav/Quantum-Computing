import numpy as np


def hadamard(n):
    """
    Returns the Hadamard matrix of size 2^n.

    Parameters:
    n (int): The exponent of 2 that determines the size of the Hadamard matrix.

    Returns:
    numpy.ndarray: The Hadamard matrix of size 2^n.
    """
    H = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])
    H_n = H
    for _ in range(n - 1):
        H_n = np.kron(H_n, H)
    return H_n


def oracle(n, solution_index):
    """
    Creates an oracle matrix for the Grover's algorithm.

    Parameters:
    - n (int): The number of qubits.
    - solution_index (int): The index of the solution state.

    Returns:
    - O (numpy.ndarray): The oracle matrix.
    """
    size = 2 ** n
    O = np.identity(size)
    O[solution_index, solution_index] = -1
    return O


def diffuser(n):
    """
    Constructs a diffuser matrix for Grover's algorithm.

    Parameters:
    n (int): The number of qubits.

    Returns:
    numpy.ndarray: The diffuser matrix.

    """
    size = 2 ** n
    I = np.identity(size)
    s = np.ones(size) / np.sqrt(size)
    D = 2 * np.outer(s, s) - I
    return D


def grover(n, solution_index):
    """
    Implements the Grover's algorithm for quantum search.

    Args:
        n (int): The number of qubits.
        solution_index (int): The index of the solution.

    Returns:
        numpy.ndarray: The final state after applying Grover's algorithm.
    """
    size = 2 ** n
    H_n = hadamard(n)
    O = oracle(n, solution_index)
    D = diffuser(n)

    state = np.zeros(size)
    state[0] = 1

    state = H_n @ state

    num_iterations = int(np.pi / 4 * np.sqrt(size))

    for _ in range(num_iterations):
        state = O @ state
        state = D @ state

    return state


if __name__ == "__main__":
    n = 3  # Número de qubits
    solution_index = 5  # Índice de la solución buscada

    result = grover(n, solution_index)
    print("Estado final:")
    print(result)

    # Verificación del estado final
    max_amplitude_index = np.argmax(np.abs(result)**2)
    print(f"Índice con mayor probabilidad: {max_amplitude_index}")
    print(f"Probabilidad: {np.abs(result[max_amplitude_index])**2}")

# Implementación del Algoritmo de Grover

Este documento describe una implementación del Algoritmo de Grover utilizando matrices de Hadamard y operadores específicos para la búsqueda cuántica. La implementación se realiza en Python utilizando la biblioteca `numpy`.

## Funciones

### `hadamard(n)`

Genera una matriz de Hadamard de tamaño \(2^n\).

**Parámetros:**

- `n` (int): El exponente de 2 que determina el tamaño de la matriz de Hadamard.

**Retorna:**

- `numpy.ndarray`: La matriz de Hadamard de tamaño \(2^n\).

```python
def hadamard(n):
    H = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])
    H_n = H
    for _ in range(n - 1):
        H_n = np.kron(H_n, H)
    return H_n
```

### `oracle(n, solution_index)`

Crea una matriz de oráculo para el Algoritmo de Grover.

**Parámetros:**

- `n` (int): El número de qubits.
- `solution_index` (int): El índice del estado solución.

**Retorna:**

- `numpy.ndarray`: La matriz de oráculo.

```python
def oracle(n, solution_index):
    size = 2 ** n
    O = np.identity(size)
    O[solution_index, solution_index] = -1
    return O
```

### `diffuser(n)`

Construye una matriz difusora para el Algoritmo de Grover.

**Parámetros:**

- `n` (int): El número de qubits.

**Retorna:**

- `numpy.ndarray`: La matriz difusora.

```python
def diffuser(n):
    size = 2 ** n
    I = np.identity(size)
    s = np.ones(size) / np.sqrt(size)
    D = 2 * np.outer(s, s) - I
    return D
```

### `grover(n, solution_index)`

Implementa el Algoritmo de Grover para búsqueda cuántica.

**Parámetros:**

- `n` (int): El número de qubits.
- `solution_index` (int): El índice del estado solución.

**Retorna:**

- `numpy.ndarray`: El estado final después de aplicar el Algoritmo de Grover.

```python
def grover(n, solution_index):
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
```

## Uso

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/msosav/Quantum-Computing.git
   cd Quantum-Computing/Grovers
   ```

1. Instalar las numpy:

   ```bash
   pip install numpy
   ```

1. Ejecutar el script:

   ```bash
   python grover.py
   ```

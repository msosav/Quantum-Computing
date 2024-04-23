# Grover's Algorithm in Python

## Imports

```python
import numpy as np
```

The code imports the numpy library (abbreviated as np here) for numerical computations. We'll use NumPy arrays to represent quantum states in this implementation.

## Oracle Function

```python
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
```

The oracle function defines a key element in Grover's algorithm. It takes two lists:

- `elements`: This represents the entire search space, containing all possible elements you want to search through.
- `marked`: This list specifies the elements you're interested in finding. These are the "marked" elements.
- The function iterates through the elements list and checks if each element is present in the marked list. If an element is found in marked, it returns -1. Otherwise, it returns 1. This function essentially creates a labeling mechanism to identify the target elements within the search space.

## Grover's Algorithm

```python
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

    for i in range(num_iterations):
        state = 2 * np.dot(oracle_matrix, state) - state
        state = state / np.linalg.norm(state)
        state = 2 * np.dot(oracle_matrix, state) - state

    return state
```

This function implements the core logic of Grover's algorithm. Here's a breakdown of the steps:

- **Initialization:**
  - `n`: This variable stores the number of elements in the search space (`len(elements)`).
  - `num_iterations`: This calculates the optimal number of iterations for Grover's algorithm based on the search space size (n). The formula uses pi (represented by np.pi) and the square root function (np.sqrt).
  - state: This is a NumPy array representing the initial quantum state. It's initialized as a uniform superposition, meaning all elements have an equal probability of being found. We achieve this by creating an array of ones (`np.ones(n)`) and dividing it by the square root of n.
- **Oracle:**
  - `oracle_matrix`: This line calls the previously defined oracle function to create a diagonal matrix. The diagonal elements will be -1 for marked elements and 1 for unmarked elements in the search space. This matrix essentially encodes the information about the target elements.
- **Grover's Iteration (loop):**
  This is the heart of the algorithm. The loop iterates for the calculated `num_iterations`.

  - **Diffusion Operator:**
    - The state is manipulated using the diffusion operator. This operator amplifies the probability of the marked states while suppressing the probability of unmarked states. It involves applying the oracle matrix (`oracle_matrix`) twice with a subtraction in between.
  - **Normalization:**
    - After each iteration, the state vector is normalized to ensure its elements' probabilities add up to 1. This is crucial to maintain a valid quantum state.
  - **Oracle (Again):**
    - The oracle matrix is applied again to further amplify the marked states.
  - **Return:**

    - The final state after the Grover iterations represents the probability amplitudes for finding each element in the search space. Measuring this state will likely point to a marked element with high probability.

## Example Usage

```python
if __name__ == "__main__":
    elements = [0, 1, 2, 3, 4, 5, 6, 7]
    marked = [3, 5]

    probabilities = grovers_algorithm(elements, marked)
    print(probabilities)
```

In this example, we define a search space (`elements`) and specify the marked elements (`marked`). We then call the `grovers_algorithm` function to run Grover's algorithm on these inputs and print the resulting probabilities.

## Running the Code

You can run the code by executing the Python script. Make sure you have the necessary dependencies (NumPy) installed. You can install NumPy using pip:

```bash
pip install numpy
```

Save the code in a Python file (e.g., `grover.py`) and run it using:

```bash
python grover.py
```

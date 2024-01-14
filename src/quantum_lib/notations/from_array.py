import numpy as np
from IPython.display import Math, Latex


def array_to_dirac_notation(superposition_array):
    """
    Convert a complex-valued array representing a quantum state in superposition
    to Dirac notation.

    Parameters:
    - superposition_array (numpy.ndarray): The complex-valued array representing
      the quantum state in superposition.

    Returns:
    str: The Dirac notation representation of the quantum state.
    """
    # Ensure the statevector is normalized
    superposition_array = superposition_array / np.linalg.norm(superposition_array)

    # Get the number of qubits
    num_qubits = int(np.log2(len(superposition_array)))

    # Initialize Dirac notation string
    dirac_notation = ""

    # Iterate through the array and add terms to the Dirac notation
    for i, amplitude in enumerate(superposition_array):
        # Skip negligible amplitudes
        if np.abs(amplitude) > 1e-10:
            # Convert the index to binary representation
            binary_rep = format(i, f"0{num_qubits}b")

            # Add the term to Dirac notation
            dirac_notation += f"{amplitude:.3f}|{binary_rep}⟩ + "

    # Remove the trailing " + " and return the result
    return dirac_notation[:-3]


def array_to_matrix_representation(array):
    """
    Convert a one-dimensional array to a column matrix representation.

    Parameters:
    - array (numpy.ndarray): The one-dimensional array to be converted.

    Returns:
    numpy.ndarray: The column matrix representation of the input array.
    """
    return array.reshape((len(array), 1))


def array_to_dirac_latex(array):
    """
    Generate LaTeX code for displaying the Dirac notation of a quantum state.

    Parameters:
    - array (numpy.ndarray): The complex-valued array representing the quantum state.

    Returns:
    Math: A Math object containing LaTeX code for displaying Dirac notation.
    """
    return Math(f"Dirac Notation:{array_to_dirac_notation(array)}")


def array_to_matrix_latex(array):
    """
    Generate LaTeX code for displaying the matrix representation of a one-dimensional array.

    Parameters:
    - array (numpy.ndarray): The one-dimensional array to be represented as a matrix.

    Returns:
    Math: A Math object containing LaTeX code for displaying the matrix representation.
    """
    matrix_representation = array_to_matrix_representation(array)
    latex = (
        "\\begin{bmatrix}\n"
        + "\\\\\n".join(map(str, matrix_representation.flatten()))
        + "\n\\end{bmatrix}"
    )
    return Math(f"Matrix Representation:{latex}")


def array_to_dirac_and_matrix_latex(array):
    """
    Generate LaTeX code for displaying both the matrix representation and Dirac notation
    of a quantum state.

    Parameters:
    - array (numpy.ndarray): The complex-valued array representing the quantum state.

    Returns:
    Latex: A Latex object containing LaTeX code for displaying both representations.
    """
    matrix_representation = array_to_matrix_representation(array)
    latex = (
        "Matrix representation\n\\begin{bmatrix}\n"
        + "\\\\\n".join(map(str, matrix_representation.flatten()))
        + "\n\\end{bmatrix}\n"
    )
    latex += f"Dirac Notation:\n{array_to_dirac_notation(array)}"
    return Latex(latex)

def matrix_to_latex(matrix, prefix=''):
    """
    Convert a NumPy matrix to its LaTeX representation.

    Parameters:
    - matrix (numpy.ndarray): The input matrix.
    - prefix (str): A string to be prepended to the LaTeX representation.

    Returns:
    IPython.display.Math: LaTeX representation of the matrix.
    """
    latex_code = f'{prefix}\\begin{{bmatrix}}\n'
    
    for row in matrix:
        latex_code += ' & '.join(map(str, row))
        latex_code += ' \\\\\n'
    
    latex_code += '\\end{bmatrix}'

    return Math(latex_code)

def complex_matrix_to_string(matrix):
    """
    Transform a matrix of complex numbers to strings truncated to 4 decimals.

    Parameters:
    - matrix (numpy.ndarray): The input matrix of complex numbers.

    Returns:
    numpy.ndarray: Matrix of strings.
    """
    def format_complex_number(x):
        if x.real == 0 and x.imag == 0:
            return '0'
        elif x.real == 0:
            return f"{x.imag:.4f}i"
        elif x.imag == 0:
            return f"{x.real:.4f}"
        else:
            return f"{x.real:.4f} + {x.imag:.4f}i" if x.imag >= 0 else f"{x.real:.4f} - {-x.imag:.4f}I"

    formatted_matrix = np.vectorize(format_complex_number)(matrix)
    return formatted_matrix
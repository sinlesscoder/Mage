import numpy as np
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Helper Functions

def generate_random_matrix(m: int, n: int):
    # Numpy random random integer
    matrix = np.random.randint(0, 10000, size=(m,n))

    # Transform it into a pandas DataFrame
    df = pd.DataFrame(matrix)

    # Change the column names
    df.columns = [f'column_{i+1}' for i in range(n)]

    return df


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    m = 5000
    n = 2

    matrix = generate_random_matrix(m, n)

    return matrix


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
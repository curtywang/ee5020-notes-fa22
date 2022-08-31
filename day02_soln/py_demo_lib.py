import numpy as np


def multiply_add(num_a: float, num_b: float, num_c: float) -> float:
    """
    Performs the multiply-accumulate operation.
    
    :example: multiply_add(1.0, 2.0, 3.0) -> 7.0
    
    :param num_a: the accumulator a
    :param num_b: the product operand b
    :param num_c: the product operand c
    :returns: a + b * c
    """
    return num_a + num_b * num_c


def multiply_add_ndarray(
    num_a: np.ndarray, 
    num_b: np.ndarray, 
    num_c: np.ndarray) -> np.ndarray:
    """
    Performs the multiply-accumulate operation.
    
    :example: multiply_add_ndarray(
                np.arange(1, 10),
                np.arange(1, 10),
                np.arange(1, 10)
              ) -> array([ 2,  6, 12, 20, 30, 42, 56, 72, 90])
    
    :param num_a: the accumulator a
    :param num_b: the product operand b
    :param num_c: the product operand c
    :returns: a + b * c
    """
    return num_a + num_b * num_c


def main() -> None:
    return


if __name__ == '__main__':
    main()

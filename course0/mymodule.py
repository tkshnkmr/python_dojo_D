"""
This script is ... brah brah ...
"""

from typing import List


def my_method_1(x_val: int, y_val: str) -> str:
    """
    My method

    Args:
        x_val (Integer): input
        y_val (str): input
    Returns:
        str
    """

    return str(x_val) + y_val


def _my_hidden_method_1(x_val: int, y_val: str) -> List:
    """
    My hidden method - weak internal use
    from mymodule import * -> won't be imported

    Args:
        x_val (Integer): input
        y_val (str): input
    Returns:
        List
    """

    return [str(x_val), y_val]

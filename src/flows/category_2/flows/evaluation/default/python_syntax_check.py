from typing import List
import ast
from promptflow import log_metric, tool


@tool
def python_syntax_check(prediction: str):
    """
    This tool checks the syntax of the prediction of a single line and returns the processed result.

    :param prediction: the prediction of a single line.
    """

    # Add your line processing logic here
    try:
        ast.parse(prediction)
        processed_result = 1
    except SyntaxError as e:
        processed_result = -1

    return processed_result
    

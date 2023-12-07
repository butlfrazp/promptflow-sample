from typing import List
from promptflow import log_metric, tool


@tool
def aggregate(syntax_checks: List[int]):
    number_of_rows_with_syntax_errors = 0
    for row in syntax_checks:
        if row == -1:
            number_of_rows_with_syntax_errors += 1

    # Log metric the aggregate result
    log_metric(key="number_of_rows_with_syntax_errors", value=number_of_rows_with_syntax_errors)
    return number_of_rows_with_syntax_errors

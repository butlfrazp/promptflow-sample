from typing import List
from promptflow import log_metric, tool


@tool
def aggregate(llm_scores: List[str]):
    # Add your aggregation logic here
    # Aggregate the results of all lines and calculate the accuracy
    aggregated_result = round((sum([int(result) for result in llm_scores]) / len(llm_scores)), 2)

    # Log metric the aggregate result
    log_metric(key="average_llm_score", value=aggregated_result)
    return aggregated_result

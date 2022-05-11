"""
File contains functions to:
- Do analysis
- Helper functions
"""
from AURIN_result import aurin_result

def get_aurin(search_by="topic", search_region="all", search_topic="all"):
    """
        This function returns the result of basic summarization in two AURIN datasets
        1. ABS - Data by Region - Land & Environment
        2. G30 Number of Motor Vehicle by Dweling Census

        Parameters
        ** search_by: str
        - "topic": search by specific topic
        - "region": search by specific region
        - "both": search by specific topic and region (both)
        - "all":  returns all analysis result 
        ** search_region: str
        Only available if search_by is "region" or "all". Can take four values "west", "east", "north", or "south".
        ** search_topic: str
        Only available if search_by is "topic" or "all". Can take two values "solar" or "electric_cars".

        return dictionary with description and analysis result
    """
    output = {}
    output["description"] = aurin_result["description"]
    output["result"] = {}
    
    if search_by == "topic":
        # Search by specific topic and all regions
        for region, analysis in aurin_result["result"].items():
            output["result"][region] = analysis[search_topic]
    elif search_by == "region":
        output["result"] = aurin_result["result"][search_region]
    elif search_by == "both":
        output["result"][region] = aurin_result["result"][search_region][search_topic]
    else:
        output = aurin_result

    return output

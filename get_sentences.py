# Installing dependencies
from subprocess import call
call(['py', 'inst_dependencies.py'])

import json


def getSentencesFromJSONDataset(filename: str) -> list:
    """
    Extracts sentences from the dataset represented as a JSON file.

    Args:
        filename (str): The name of the JSON file from which to extract sentences.

    Returns:
        List of the sentences from the JSON file.
    """

    # Open the JSON file and load its contents
    with open("sample.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Extract the "text" values and returning it as a result
    return [entry["text"] for entry in data]

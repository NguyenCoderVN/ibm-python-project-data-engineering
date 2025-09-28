"""NguyenCoderVN"""

import glob
import xml.etree.ElementTree as ET
from datetime import datetime

import pandas as pd

LOG_FILE = "log_file.txt"
TARGET_FILE = "transformed_data.csv"


def extract_from_csv(file_to_process):

    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract_from_json(file_to_process):
    """
    extract function.
    Args:
        file_to_process (Any): Description of file_to_process.
    Returns:
        None
    """
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


def extract_from_xml(file_to_process):
    """
    extract function.
    Args:
        file_to_process (Any): Description of file_to_process.
    Returns:
        None
    """
    dataframe = pd.DataFrame(
        data=[], columns=["name", "height", "weight"]  # type: ignore
    )  # create an empty frame to hold extracted data
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text  # type: ignore
        height = float(person.find("height").text)  # type:ignore
        weight = float(person.find("weight").text)  # type: ignore
        dataframe = pd.concat(
            [
                dataframe,
                pd.DataFrame([{"name": name, "height": height, "weight": weight}]),
            ],
            ignore_index=True,
        )
    return dataframe


def extract():
    """
    extract function.
    Returns:
        None
    """
    extracted_data = pd.DataFrame(data=[], columns=["name", "height", "weight"])  # type: ignore

    for csvfile in glob.glob("*.csv"):
        if csvfile != TARGET_FILE:
            extracted_data = pd.concat(
                [extracted_data, pd.DataFrame(extract_from_csv(csvfile))],
                ignore_index=True,
            )

    for jsonfile in glob.glob("*.json"):
        if jsonfile != TARGET_FILE:
            extracted_data = pd.concat(
                [extracted_data, pd.DataFrame(extract_from_json(jsonfile))],
                ignore_index=True,
            )

    for xmlfile in glob.glob("*.xml"):
        if xmlfile != TARGET_FILE:
            extracted_data = pd.concat(
                [extracted_data, pd.DataFrame(extract_from_xml(xmlfile))],
                ignore_index=True,
            )
    return extracted_data


def transform(data):
    """Convert inches to meters and round off to two decimals
        1 inch is 0.0254 meters
    Convert pounds to kilograms and round off to two decimals
        1 pound is 0.45359237 kilograms
    """
    data["height"] = round(data.height * 0.0254, 2)
    data["weight"] = round(data.weight * 0.45359237, 2)

    return data


def load_data(target_file, data):
    """
    load function.
    Args:
        target_file (Any): Description of target_file.
        data (Any): Description of data.
    Returns:
        None
    """
    data.to_csv(target_file)


def log_progress(message):
    """
    log function.
    Args:
        message (Any): Description of message.
    Returns:
        None
    """
    timestamp_format = "%Y-%h-%d-%H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(timestamp + "," + message + "\n")


# Log the initialization of the ETL process
log_progress("ETL Job Started")

# Log the beginning of the Extraction process
log_progress("Extract phase Started")
extracted_data = extract()

# Log the completion of the Extraction process
log_progress("Extract phase Ended")

# Log the beginning of the Transformation process
log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data")
print(transformed_data)

# Log the completion of the Transformation process
log_progress("Transform phase Ended")

# Log the beginning of the Loading process
log_progress("Load phase Started")
load_data(TARGET_FILE, transformed_data)

# Log the completion of the Loading process
log_progress("Load phase Ended")

# Log the completion of the ETL process
log_progress("ETL Job Ended")

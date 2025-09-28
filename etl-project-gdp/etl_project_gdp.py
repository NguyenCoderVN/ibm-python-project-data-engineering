"""NguyenCoderVN"""

import sqlite3
from datetime import datetime
from typing import List

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


def greet_all(names: List[str]) -> None:
    for name in names:
        print("Hello", name)


greet_all(["Alice", "Bob"])  # ✅ hợp lệ
greet_all([1, 2, 3])  # ❌ lỗi type (int thay vì str)
greet_all("Alice")  # ❌ lỗi type (string thay vì list[str])

# URL = (
#     "https://web.archive.org/web/20230902185326/",
#     "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29",
# )
_ABC = "qbvc"
URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
DB_NAME = "World_Economies.db"
TABLE_NAME = "Countries_by_GDP"
TABLE_ATTRIBS = ["Country", "GDP_USD_millions"]
CSV_PATH = "./Countries_by_GDP.csv"


def extract(url, table_attribs):

    html_parser = requests.get(url).text
    # data = BeautifulSoup(html_parser, "html.parser")
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all("tbody")
    rows = tables[2].find_all("tr")
    for row in rows:
        col = row.find_all("td")
        if col:
            if col[0].find("a") is not None and "-" not in col[2]:
                data_dict = {
                    "Country": col[0].a.contents[0],
                    "GDP_USD_millions": col[2].contents[0],
                }
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)

    return df


def transform(df):
    """This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe."""

    gdp_list = []
    # Lặp qua từng phần tử trong cột GDP
    for x in df["GDP_USD_millions"].tolist():
        try:
            # Loại bỏ dấu phẩy và chuyển đổi sang float
            gdp_value = float("".join(x.split(",")))
            gdp_list.append(gdp_value)
        except ValueError:
            # Nếu xảy ra lỗi ValueError (không thể chuyển đổi chuỗi thành số),
            # thêm giá trị NaN vào danh sách
            gdp_list.append(np.nan)

    # Tiếp tục các bước biến đổi còn lại
    gdp_list = [np.round(x / 1000, 2) for x in gdp_list]
    df["GDP_USD_millions"] = gdp_list
    df = df.rename(columns={"GDP_USD_millions": "GDP_USD_billions"})
    return df


def load_to_csv(df, csv_path):
    """This function saves the final dataframe as a `CSV` file
    in the provided path. Function returns nothing."""
    df.to_csv(csv_path)


def load_to_db(df, sql_connection, table_name):
    """This function saves the final dataframe as a database table
    with the provided name. Function returns nothing."""
    df.to_sql(table_name, sql_connection, if_exists="replace", index=False)


def run_query(query_statement, sql_connection):
    """This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing."""
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


def log_progress(message):
    """This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing"""
    timestamp_format = "%Y-%h-%d-%H-%M-%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_log.txt", "a") as f:
        f.write(timestamp + ":" + message + "\n")


""" Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function."""


log_progress("Preliminaries complete. Initiating ETL process")

df = extract(URL, TABLE_ATTRIBS)

log_progress("Data extraction complete. Initiating Transformation process")

df = transform(df)

log_progress("Data transformation complete. Initiating loading process")

load_to_csv(df, CSV_PATH)

log_progress("Data saved to CSV file")

sql_connection = sqlite3.connect("World_Economies.db")

log_progress("SQL Connection initiated.")

load_to_db(df, sql_connection, TABLE_NAME)

log_progress("Data loaded to Database as table. Running the query")

query_statement = f"SELECT * from {TABLE_NAME} WHERE GDP_USD_billions >= 100"
run_query(query_statement, sql_connection)

log_progress("Process Complete.")

sql_connection.close()

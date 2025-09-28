import sqlite3

import pandas as pd

conn = sqlite3.connect("STAFF.db")

TABLE_NAME = "Department"
ATTRIBUTE_LIST = ["DEPT_ID", "DEP_NAME", "MANAGER_ID", "LOC_ID"]

FILE_PATH = "Departments.csv"
df = pd.read_csv(FILE_PATH, names=ATTRIBUTE_LIST)

df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
print("Table is ready")

data_dict = {
    "DEPT_ID": [100],
    "DEP_NAME": ["John"],
    "MANAGER_ID": [30010],
    "LOC_ID": ["L0010"],
}

data_append = pd.DataFrame(data_dict)

data_append.to_sql(TABLE_NAME, conn, if_exists="append", index=False)
print("Data appended successfully")

query_statement = f"SELECT * FROM {TABLE_NAME}"
query_output = pd.read_sql(query_statement, conn)
print(query_output)

conn.close()

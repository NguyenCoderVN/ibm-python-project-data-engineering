import sqlite3

import pandas as pd

conn = sqlite3.connect("STAFF.db")

TABLE_NAME = "INSTRUCTOR"
ATTRIBUTE_LIST = ["ID", "FNAME", "LNAME", "CITY", "CCODE"]

FILE_PATH = "INSTRUCTOR.csv"
df = pd.read_csv(FILE_PATH, names=ATTRIBUTE_LIST)

df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
print("Table is ready")

query_statement = f"SELECT * FROM {TABLE_NAME}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT FNAME FROM {TABLE_NAME}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT COUNT(*) FROM {TABLE_NAME}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

data_dict = {
    "ID": [100],
    "FNAME": ["John"],
    "LNAME": ["Doe"],
    "CITY": ["Paris"],
    "CCODE": ["FR"],
}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(TABLE_NAME, conn, if_exists="append", index=False)
print("Data appended successfully")
conn.close()

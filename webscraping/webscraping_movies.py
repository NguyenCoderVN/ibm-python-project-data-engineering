"""NguyenCoderVN"""

import sqlite3

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = (
    "https://web.archive.org/web/20230902185655/"
    "https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
)
DB_NAME = "Movies.db"
TABLE_NAME = "Top_50"
CSV_PATH = "top_50_films.csv"
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])  # type: ignore
COUNT = 0

html_page = requests.get(URL).text
data = BeautifulSoup(html_page, "html.parser")

tables = data.find_all("tbody")
rows = tables[0].find_all("tr")

for row in rows:
    if COUNT < 50:
        col = row.find_all("td")
        if len(col) != 0:
            data_dict = {
                "Average Rank": int(col[0].text),
                "Film": str(col[1].text),
                "Year": int(col[2].text),
            }
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            COUNT += 1
    else:
        break

print(df)

conn = sqlite3.connect(DB_NAME)
df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
conn.close()

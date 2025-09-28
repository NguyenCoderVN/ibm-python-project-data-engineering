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
TABLE_NAME = "Top_5"
CSV_PATH = "Top_5_rank.csv"

# Fetch HTML
response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
movies = []

# Extract first 50 movies
tables = soup.find_all("tbody")
rows = tables[1].find_all("tr")
for row in rows[:5]:
    col = row.find_all("td")
    if col:
        movies.append(
            {
                "Rank": int(col[0].text),
                "Decade": col[1].text.strip(),
                "Occurrences": int(col[2].text),
            }
        )

df = pd.DataFrame(movies)

# Save to CSV
df.to_csv(CSV_PATH, index=False)

# Save to SQLite
with sqlite3.connect(DB_NAME) as conn:
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

print(df)

import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Art_Tatum")

soup = bs4.BeautifulSoup(response.text, "html.parser")

headings = []

for item in soup.select('.mw-heading'):
    headings.append(item.text)

import pandas as pd

heading_df = pd.DataFrame()
heading_df["headings"] = pd.Series(headings).values
print(heading_df["headings"])

heading_df.to_csv("heading_results.csv")
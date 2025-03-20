"""
Simple program that extracts a csv file found from a URL.
using only pandas. Specifically, we are going to extract all the CSV files found at the website
https://www.football-data.co.uk/data.php
"""

import pandas as pd

df_japan = pd.read_csv("https://www.football-data.co.uk/new/JPN.csv") #websites are not the only thing that you can insert as a parameter - see https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
print(df_japan)

#below, we will change some of the columns in case you do not know what 'FGHT' or 'FTAG' means:
#see the GFG webpage that describes the df.rename() function: https://www.w3schools.com/python/pandas/ref_df_rename.asp
df_japan.rename(columns={'FTHG' : "home_goals",
                         'FTAG' : "away_goals"})

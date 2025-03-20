"""
Simple program that extracts a csv file found from a URL using only pandas. Specifically, we are going to extract all the CSV files found 
at the website https://www.football-data.co.uk/data.php
"""

import pandas as pd

df_japan = pd.read_csv("https://www.football-data.co.uk/new/JPN.csv") #URL's are not the only thing that you can insert as a parameter - see https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html for a full list of parameters
print(df_japan)

#below, we will change some of the column names in case you do not know what they mean (note we changed 'HG' and 'AG' to home_goals and away_goals):
#see the GFG webpage that describes the df.rename() function: https://www.w3schools.com/python/pandas/ref_df_rename.asp

df_japan.rename(columns={'HG' : "home_goals",
                         'AG' : "away_goals"}, inplace=True)
df_japan.to_csv("./Table Extraction/output.csv", index=False)  #save without row numbers

"""
Notice above that we used inplace=True as a parameter. If we did not include this (i.e. inplace = False), the rename function would return a new dataframe with updated
column names, however we would need to create a new variable to hold this new dataframe.
"""
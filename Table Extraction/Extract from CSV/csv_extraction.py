"""
Simple program that extracts a csv file found from a URL using only pandas. csv files are found at the website https://www.football-data.co.uk/data.php within this website
we are accessing the japan league.
"""

import pandas as pd

df_japan = pd.read_csv("https://www.football-data.co.uk/new/JPN.csv") #URL's are not the only thing that you can insert as a parameter - see https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html for a full list of parameters

#if you were to print df_japan directly above this comment, you would see the dataframe table output in the terminal window. However you might see some terms in the columns
# that you are unfamiliar with, such as 'HG' or 'AG' etc. below, we will change some of the column names in case you do not know what they mean (note we changed 'HG' and 'AG' to home_goals and away_goals):

df_japan.rename(columns={'HG' : "home_goals",
                         'AG' : "away_goals"}, inplace=True)
df_japan.to_csv("./Table Extraction/japan.csv", index=False)  #save this into a csv file in our current directory without row numbers (index)

#see the GFG webpage that describes the df.rename() function: https://www.w3schools.com/python/pandas/ref_df_rename.asp

"""
Notice above that we used inplace=True as a parameter. If we did not include this (i.e. inplace = False), the rename function would return a new dataframe with updated
column names, however we would need to create a new variable to hold this new dataframe.
"""
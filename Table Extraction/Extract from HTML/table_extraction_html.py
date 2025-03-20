"""
Simple program that imports pandas, reads an html file (in this case, it is a wikipedia page that 
includes a table of all the simpsons episodes and other information), and prints out the table for season 1 of the simpsons.

Note that there must be <table></table> html tag(s) included in the html file in order for pandas to successfully recognize
and read the table. 
"""

import pandas as pd 

simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')

print(len(simpsons))        #prints 24, since there are 24 tables that were found at the HTML link provided.

print(f"Season 1: \n\n{simpsons[1]}")
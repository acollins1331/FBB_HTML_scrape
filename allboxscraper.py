'''
Created on Feb 7, 2018

@author: Adam
'''

import requests
import pandas as pd

dfs = pd.DataFrame()

#Scrape all 120x15 box scores of the season
url = 'http://thatsimlife.club/TMBSL5/2003/PRESEASON/boxes/{}-{}.html'
for i in range(1, 165):
    html = requests.get(url.format(i, 1)).content
    try:
            df_list = pd.read_html(html)
    except:
        continue
    for j in range(1, 15):
        html = requests.get(url.format(i, j)).content
        try:
            df_list = pd.read_html(html, flavor=None, header=None, index_col=None, skiprows=[0] )
        except:
            continue
        df0 = df_list[0]
        df1 = df_list[-1]
        df2 = df_list[-2]
        df1.drop(df1.tail(1).index,inplace=True)
        print("("+str(i)+","+str(j)+")")
        print(df1)
        print(df2)
        dfs = dfs.append(df1)
        dfs = dfs.append(df2)
dfs.to_csv('D:/Scrape/allboxscore.csv')
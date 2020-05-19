'''
Created on Feb 7, 2018

@author: Adam
'''

import requests
import pandas as pd

url = 'http://thatsimlife.club/TMBSL5/2003/fa/fa-name.htm'
html = requests.get(url).content
df_list = pd.read_html(html, 'Name')
df0 = df_list[0]
df1 = df_list[-1]
df2 = df_list[-2]
dff = df0
dff = dff.append(df1)
dff = dff.append(df2)
print (dff)
dff.to_csv('D:/Scrape/FA.csv')
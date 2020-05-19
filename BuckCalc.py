'''
Created on Feb 7, 2018

@author: Adam
'''
import requests
import pandas as pd
import numpy as np

raw_data = pd.read_csv('D:/Scrape/2000boxscore.csv')
       
df = pd.read_csv('D:/Scrape/2000boxscore.csv', names = ['Name', 'POS', 'MIN', 'FG', 'FGA', 'TP', '3PA', 'FT', 'FTA', 'REB', 'A', 'PF', 'STL', 'TO', 'BL', 'PTS', 'URL'])                

df.groupby(['Name']).groups.keys()

#print(df.groupby(['Name']).groups.keys())

#print(df.groupby('Name')['PTS'].std())

df.insert(17, 'Reward', np.nan)
df.insert(18, 'Bux', np.nan)
df.insert(19, 'TPTSBux', np.nan)
df.insert(20, 'TREBBux', np.nan)
df.insert(21, 'TABux', np.nan)
df.insert(22, 'TBLBux', np.nan)
df.insert(23, 'TSTLBux', np.nan)
df.insert(24, 'TTPBux', np.nan)
df.insert(25, 'TFTBux', np.nan)

df.loc[ (df.PTS >= 45) & (df.Name != 'TEAM TOTALS') , 'Reward'] = '45 pts'
df.loc[ (df.PTS >= 45) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 25
df.loc[ (df.PTS >= 50) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '50 pts'
df.loc[ (df.PTS >= 50) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 50
df.loc[ (df.PTS >= 60) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '60 pts'
df.loc[ (df.PTS >= 60) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 100

df.loc[ (df.REB >= 25) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '25 reb'
df.loc[ (df.REB >= 25) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 100
df.loc[ (df.REB >= 30) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '25 reb'
df.loc[ (df.REB >= 30) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 200

df.loc[ (df.A >= 17) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '17 ast'
df.loc[ (df.A >= 17) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 75
df.loc[ (df.A >= 20) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '20 ast'
df.loc[ (df.A >= 20) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 150
df.loc[ (df.A >= 25) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '25 ast'
df.loc[ (df.A >= 25) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 300

df.loc[ (df.BL >= 9) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '9 blk'
df.loc[ (df.BL >= 9) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 75
df.loc[ (df.BL >= 12) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '12 blk'
df.loc[ (df.BL >= 12) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 150

df.loc[ (df.STL >= 7) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '7 stl'
df.loc[ (df.STL >= 7) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 75
df.loc[ (df.STL >= 10) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '10 stl'
df.loc[ (df.STL >= 10) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 150

df.loc[ (df.TP >= 8) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '8 3P'
df.loc[ (df.TP >= 8) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 100
df.loc[ (df.TP >= 10) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '10 3P'
df.loc[ (df.TP >= 10) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 200

df.loc[ (df.FG >= 15) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '15 FG'
df.loc[ (df.FG >= 15) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 25
df.loc[ (df.FG >= 20) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '20 FG'
df.loc[ (df.FG >= 20) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 100
df.loc[ (df.FG >= 25) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '25 FG'
df.loc[ (df.FG >= 25) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 200

df.loc[ (df.FT >= 15) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '15 FT'
df.loc[ (df.FT >= 15) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 50
df.loc[ (df.FT >= 20) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '20 FT'
df.loc[ (df.FT >= 20) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 100
df.loc[ (df.FT >= 25) & (df.Name != 'TEAM TOTALS')  , 'Reward'] = '25 FT'
df.loc[ (df.FT >= 25) & (df.Name != 'TEAM TOTALS')  , 'Bux'] = 200

df.loc[ (df.REB >= 25) & (df.PTS >= 20) & (df.Name != 'TEAM TOTALS') , 'Reward'] = '20/20'
df.loc[ (df.REB >= 25) & (df.PTS >= 20)  & (df.Name != 'TEAM TOTALS') , 'Bux'] = 100

df.loc[ (df.REB >= 10) & (df.PTS >= 10) & (df.A >= 10) & (df.Name != 'TEAM TOTALS') , 'Reward'] = 'tripdub'
df.loc[ (df.REB >= 10) & (df.PTS >= 10) & (df.A >= 10) & (df.Name != 'TEAM TOTALS') , 'Bux'] = 150

df.loc[ (df.Name == 'TEAM TOTALS') & (df.PTS > 150), 'Reward'] = '150 team pts'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.PTS > 150), 'TPTSBux'] = 50
df.loc[ (df.Name == 'TEAM TOTALS') & (df.PTS > 160), 'Reward'] = '160 team pts'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.PTS > 160), 'TPTSBux'] = 100
df.loc[ (df.Name == 'TEAM TOTALS') & (df.PTS > 170), 'Reward'] = '170 team pts'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.PTS > 170), 'TPTSBux'] = 200

df.loc[ (df.Name == 'TEAM TOTALS') & (df.REB > 70), 'Reward'] = '70 team reb'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.REB > 70), 'TREBBux'] = 100
df.loc[ (df.Name == 'TEAM TOTALS') & (df.REB > 80), 'Reward'] = '80 team reb'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.REB > 80), 'TREBBux'] = 200

df.loc[ (df.Name == 'TEAM TOTALS') & (df.A > 35), 'Reward'] = '35 team ast'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.A > 35), 'TABux'] = 100
df.loc[ (df.Name == 'TEAM TOTALS') & (df.A > 40), 'Reward'] = '40 team ast'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.A > 40), 'TABux'] = 200

df.loc[ (df.Name == 'TEAM TOTALS') & (df.BL > 15), 'Reward'] = '15 team blk'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.BL > 15), 'TBLBux'] = 25
df.loc[ (df.Name == 'TEAM TOTALS') & (df.BL > 20), 'Reward'] = '20 team blk'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.BL > 20), 'TBLBux'] = 100
df.loc[ (df.Name == 'TEAM TOTALS') & (df.BL > 25), 'Reward'] = '25 team blk'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.BL > 25), 'TBLBux'] = 200

df.loc[ (df.Name == 'TEAM TOTALS') & (df.STL > 15), 'Reward'] = '15 team stl'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.STL > 15), 'TSTLBux'] = 50
df.loc[ (df.Name == 'TEAM TOTALS') & (df.STL > 20), 'Reward'] = '20 team stl'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.STL > 20), 'TSTLBux'] = 100
df.loc[ (df.Name == 'TEAM TOTALS') & (df.STL > 25), 'Reward'] = '25 team stl'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.STL > 25), 'TSTLBux'] = 200

df.loc[ (df.Name == 'TEAM TOTALS') & (df.TP > 12), 'Reward'] = '12 team 3p'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.TP > 12), 'TTPBux'] = 50
df.loc[ (df.Name == 'TEAM TOTALS') & (df.TP > 15), 'Reward'] = '15 team 3p'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.TP > 15), 'TTPBux'] = 100
df.loc[ (df.Name == 'TEAM TOTALS') & (df.TP > 20), 'Reward'] = '20 team 3p'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.TP > 20), 'TTPBux'] = 200

df.loc[ (df.Name == 'TEAM TOTALS') & (df.FT > 35), 'Reward'] = '35 team FT'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.FT > 35), 'TFTBux'] = 50
df.loc[ (df.Name == 'TEAM TOTALS') & (df.FT > 40), 'Reward'] = '40 team FT'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.FT > 40), 'TFTBux'] = 100
df.loc[ (df.Name == 'TEAM TOTALS') & (df.FT > 45), 'Reward'] = '45 team FT'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.FT > 45), 'TFTBux'] = 150
df.loc[ (df.Name == 'TEAM TOTALS') & (df.FT > 50), 'Reward'] = '50 team FT'
df.loc[ (df.Name == 'TEAM TOTALS') & (df.FT > 50), 'TFTBux'] = 200

df.to_csv('D:/Scrape/boxscorewrewards.csv')

rf = df.dropna(subset=['Reward'])

print(rf)

rf.to_csv('D:/Scrape/rewards.csv')
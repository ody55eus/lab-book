# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:25:21 2020

@author: JP
"""

import pandas as pd

# Define Measurement Numbers for different Angles
a = {-90: [155, 0],
     -85: [152, 153],
     -80: [148, 149],
     -75: [138, 139],
     -70: [134, 136],
     -65: [131, 132],
     -60: [128, 129],
     -55: [125, 126],
     -50: [122, 123],
     -45: [119, 120],
     -40: [143, 144],
     -35: [113, 114],
     -30: [110, 111],
     -25: [107, 108],
     -20: [104, 105],
     -15: [101, 102],
     -10: [98, 99],
     -5: [95, 96],
     0: [54, 55],
     5: [51, 52],
     10: [48, 49],
     15: [45, 46],
     20: [42, 43],
     25: [39, 40],
     30: [36, 37],
     35: [32, 34],
     40: [29, 30],
     45: [23, 22],
     50: [79, 80],
     55: [76, 77],
     60: [73, 74],
     65: [70, 71],
     70: [67, 68],
     75: [64, 65],
     80: [61, 62],
     85: [58, 59],
     90: [57, 0],
     95: [82, 83],
     100: [85, 86],
     105: [88, 89],
     110: [91, 93]}

df = pd.DataFrame(a).T
df.index.name = 'Angle'
df.rename({0: 'Down', 1: 'Up'}, axis=1, inplace=True)
df.to_csv('angles.csv')

f = open('angles.md', 'w')
label = ' | {:<8} '*4
items = ['Angle', 'Down', 'Up',]
f.write(label.format(*(items + ['\n'])))
f.write(('|:%8s '*4) % tuple(['-'*8]*3 + ['\n']))
df['Angle'] = df.index.map('{}deg'.format)
link = '[m{0}](Hloop/m{0})'
df.Down = df.Down.map(link.format)
df.Up = df.Up.map(link.format)
f.writelines([label.format(*[df.loc[a,_] for _ in items] + ['\n'] \
                           ) for a in df.index]
             )
f.close()

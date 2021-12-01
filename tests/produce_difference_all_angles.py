# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:59:57 2020

@author: JP
"""

# Basic Plotting libraries
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Math / Science Libraries
import pandas as pd
import numpy as np
import scipy

import logging # System Modules

logging.basicConfig(level=logging.WARNING)

# Plotting parameters
params = {
    'figure.dpi': 300,
    'figure.figsize': (16,9),
    'figure.subplot.hspace': 0.3,
    'figure.subplot.wspace': 0.3,
    'savefig.transparent': False,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
}
matplotlib.rcParams.update(params)


import ana
#eva = ana.HandleM(directory='data')

#### Hysteresis Loops
# Define Measurement Numbers for different Angles
a = {-90: [155],
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
     90: [57],
     95: [82, 83],
     100: [85, 86],
     105: [88, 89],
     110: [91, 93]}

meas = {}
df = pd.DataFrame({}, dtype=np.float64)
fig, ax = plt.subplots()
for angle, meas_nr in a.items():
    if np.abs(angle) == 90:
        nr = meas_nr[0]
        meas[nr] = ana.Hloop(nr)
        meas[nr].fit()
        #meas[nr].calculate_fitted_strayfield()
        up = meas[nr].up_fitted
        down = meas[nr].down_fitted

        for structure in ['Plusses', 'Crosses']:
            if structure == 'Plusses':
                f_up = scipy.interpolate.interp1d(up.B, up.Vx8)
                f_down = scipy.interpolate.interp1d(down.B, down.Vx8)
            else:
                f_up = scipy.interpolate.interp1d(up.B, up.Vx9)
                f_down = scipy.interpolate.interp1d(down.B, down.Vx9)
            B_ext = np.linspace(up.B.min(), up.B.max(), int(1e5))
            B_stray = f_down(B_ext) - f_up(B_ext)

            df['B_%s' % (angle)] = B_ext
            df['dVH_%s_%s' % (angle, structure)] = B_stray
            ax.plot(B_ext, B_stray, label='%s: %s' % (angle, structure))
    else:
        for nr in meas_nr:
            meas[nr] = ana.Hloop(nr)
            B_ext, B_stray = meas[nr].get_downminusup()
            df['B_%s' % (angle)] = B_ext
            df['dVH_%s_%s' % (angle, meas[nr].data['Structure'])] = B_stray
            ax.plot(B_ext, B_stray)
            
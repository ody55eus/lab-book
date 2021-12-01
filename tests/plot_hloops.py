# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:53:14 2020

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
eva = ana.HandleMeasurements(directory='data')

m1 = ana.Hloop_Measurement(408)
m2 = ana.Hloop_Measurement(409)

for m in [m1, m2]:
    fig, ax = plt.subplots()
    #m1.plot_strayfield(ax)
    plt.plot(m.up.B, m.up['Sample Temp'])
    plt.plot(m.down.B, m.down['Sample Temp'])

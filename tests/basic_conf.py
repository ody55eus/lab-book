# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:02:13 2020

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
import re # Regular Expressions
from glob import glob

logging.basicConfig(level=logging.WARNING)

# Plotting parameters
params = {
    'figure.dpi': 300,
    'figure.figsize': (11.69,8.27),
    'figure.subplot.hspace': 0.3,
    'figure.subplot.wspace': 0.3,
    'savefig.transparent': False,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
}
matplotlib.rcParams.update(params)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('EVA-SR830DAQ')

import ana

ana.set_sns(default=True, grid=True, 
            size='paper', style='ticks', latex=True)


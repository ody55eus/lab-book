# Basic Plotting libraries
import ipympl
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Math / Science Libraries
import pandas as pd
import numpy as np
import scipy

import logging # System Modules
import re # Regular Expressions
import os
from glob import glob

logging.basicConfig(level=logging.WARNING)

import ana
from spectrumanalyzer import SpectrumAnalyzer

# Plotting parameters
params = {
    'figure.dpi': 300,
    'figure.figsize': (12,8),
    #'figure.subplot.hspace': 0.3,
    #'figure.subplot.wspace': 0.3,
    'savefig.transparent': True,
    'savefig.bbox': 'tight',
    #'savefig.pad_inches': 0.1,
}
mpl.rcParams.update(params)

default_styling = [['science'], {'context': 'paper', 
                                 'style': 'white',
                                 'palette': 'bright',
                                }]

def set_style(styling=default_styling):
    """
    Args:
        styling:
    """
    plt_style, sns_style = styling
    sns.set(**sns_style)
    plt.style.use(*plt_style)
#ana.set_sns(default=True, grid=True, 
#            size='paper', style='ticks', latex=True)
#set_style()

# Save Plots to file
def save_plot(name, kind='pgf', dpi=None):
    """
    Args:
        name:
        kind:
        dpi:
    """
    if not os.path.exists('img'):
        os.makedirs('img')
    if kind == 'pgf':
        matplotlib.use("pgf")
        matplotlib.rcParams.update({
            "pgf.texsystem": "pdflatex",
            'font.family': 'serif',
            'text.usetex': True,
            'pgf.rcfonts': False,
        })

    plt.show()
    if dpi == None:
        plt.savefig('img/%s.%s' % (name, kind))
    else:
        plt.savefig('img/%s.%s' % (name, kind), dpi=dpi)


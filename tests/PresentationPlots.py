# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:20:14 2020

@author: Jonathan Pieper
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
eva = ana.HandleM(directory='data')

m = ana.Hloop(57)

#### Hysteresis Loops
# Define Measurement Numbers for different Angles
a = {}
a[-85] = [152,153]
a[-80] = [148,149]
a[-75] = [138,139]
a[-70] = [134,136]
a[-70] = [134,136]
a[-65] = [131,132]
a[-60] = [128,129]
a[-55] = [125,126]
a[-50] = [122,123]
a[-45] = [119,120]
a[-40] = [143,144]
a[-35] = [113,114]
a[-30] = [110,111]
a[-25] = [107,108]
a[-20] = [104,105]
a[-15] = [101,102]
a[-10] = [98,99]
a[-5] = [95,96]
a[0] = [54,55]
a[5] = [51,52]
a[10] = [48,49]
a[15] = [45,46]
a[20] = [42,43]
a[25] = [39,40]
a[30] = [36,37]
a[35] = [32,34]
a[40] = [29,30]
#a[42.5] = [26,27]
a[45] = [23,22]
a[60] = [73,74]
a[65] = [70,71]
a[70] = [67,68]
a[75] = [64,65]
a[80] = [61,62]
a[85] = [58,59]
a[90] = [57]
a[95] = [82,83]
a[100] = [85,86]
a[105] = [88,89]
a[110] = [91,93]

meas = {}
def plot_single_hloop(nr=a[0], filename='hloop-single-1', **kwargs):
    """Plots a single measurement. Default: 0deg

    Args:
        nr:
        filename (Str, optional): File to write. The default is
            'hloop-compare-1'.
        **kwargs (TYPE): DESCRIPTION.

    Returns:
        hloop-compare-1.pdf:
    """
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(16,12))
    
    ana.set_sns(size='talk', style='ticks', palette='deep',
                     grid=True, latex=True)
    meas[nr] = ana.Hloop(nr)
    meas[nr].plot_strayfield(ax)
    ax.set_xlim(*kwargs.get('xlim', (-250, 250)))
    if kwargs.get('ylim'):
        ax.set_ylim(*kwargs.get('ylim'))

    with sns.color_palette('deep'):
        ana.set_sns(size='talk', style='ticks',
                         grid=True, latex=True)
        inset = inset_axes(ax, width='100%', height='90%', 
                       bbox_to_anchor=(.64, .06, .35, .35),
                       bbox_transform=ax.transAxes)
        max_b = meas[nr].up.B.max()
        inset.plot([-max_b, max_b], [0, 0], 'r--', linewidth=.75)
        B_ext, B_stray = meas[nr].get_downminusup_strayfield()
        inset.plot(B_ext, B_stray)
        inset.set_ylabel("$\Delta B_z\\;[\\mathrm{mT}]$")
        inset.set_title("Difference")
        inset.set_xlim(*kwargs.get('xlim', (-250, 250)))

    plt.savefig("%s.pdf" % filename)

def plot_hloops(to_show=a[0]+a[45], filename='hloop-compare-1', **kwargs):
    """Compares Plusses and Crosses between two angles (4 Subplots). Default: 0
    and 45

    Args:
        to_show (List, optional): List of 4 Angles. The default is a[0]+a[45].
        filename (Str, optional): File to write. The default is
            'hloop-compare-1'.
        **kwargs (TYPE): DESCRIPTION.

    Returns:
        hloop-compare-1.pdf:
    """
    fig, axes = plt.subplots(2, 2, figsize=(16,12))
    for i, nr in enumerate(to_show):
        ax = axes[i//2][i%2]
        ana.set_sns(size='talk', style='ticks', palette='deep',
                         grid=True, latex=True)
        meas[nr] = ana.Hloop(nr)
        meas[nr].plot_strayfield(ax)
        ax.set_xlim(-250, 250)
        if nr in [54]:
            ax.set_ylim(0, 4.5)
        if nr in [55]:
            ax.set_xlim(-300, 300)
            ax.set_ylim(-0.8, 4.45)
        if nr in [22,23]:
            ax.set_xlim(-150, 150)

        with sns.color_palette('deep'):
            ana.set_sns(size='talk', style='ticks',
                             grid=True, latex=True)
            inset = inset_axes(ax, width='100%', height='90%', 
                           bbox_to_anchor=(.65, .09, .35, .35),
                           bbox_transform=ax.transAxes)
            max_b = meas[nr].up.B.max()
            inset.plot([-max_b, max_b], [0, 0], 'r--', linewidth=.75)
            B_ext, B_stray = meas[nr].get_downminusup_strayfield()
            inset.plot(B_ext, B_stray)
            inset.set_ylabel("$\Delta B_z\\;[\\mathrm{mT}]$")
            inset.set_title("Difference")
            inset.set_xlim(-250, 250)
            if nr in [55]:
                inset.set_xlim(-300, 300)
            if nr in [22,23]:
                inset.set_xlim(-150, 150)

    plt.savefig("%s.pdf" % filename)

def plot_hloops_95(to_show=a[95]+a[-85], filename='hloop-compare-95', **kwargs):
    """Compares +95/100/105/110deg with -85/80/75/70deg for (180deg Comparison)

    Args:
        to_show (TYPE, optional): DESCRIPTION. The default is a[95]+a[-85].
        filename (TYPE, optional): DESCRIPTION. The default is
            'hloop-compare-95'.
        **kwargs (TYPE): DESCRIPTION.

    Returns:
        hloop-compare-95.pdf:
    """
    fig, axes = plt.subplots(2, 2, figsize=(16,12))
    for i, nr in enumerate(to_show):
        ax = axes[i//2][i%2]
        ana.set_sns(size='talk', style='ticks', palette='deep',
                         grid=True, latex=True)
        meas[nr] = ana.Hloop(nr)
        meas[nr].plot_strayfield(ax)
        if kwargs.get('xlim'):
            ax.set_xlim(*kwargs.get('xlim'))
        else:
            ax.set_xlim(-750, 750)
        if meas[nr].data['Structure'] == 'Crosses' and kwargs.get('crosses_xlim'):
            ax.set_xlim(*kwargs.get('crosses_xlim'))

        with sns.color_palette('deep'):
            ana.set_sns(size='talk', style='ticks',
                             grid=True, latex=True)
            inset = inset_axes(ax, width='100%', height='90%', 
                           bbox_to_anchor=(.65, .09, .35, .35),
                           bbox_transform=ax.transAxes)
            max_b = meas[nr].up.B.max()
            inset.plot([-max_b, max_b], [0, 0], 'r--', linewidth=.75)
            B_ext, B_stray = meas[nr].get_downminusup_strayfield()
            inset.plot(B_ext, B_stray)
            #inset.set_ylabel("$\Delta B_z\\;[\\mathrm{mT}]$")
            inset.set_title("Difference")
            if kwargs.get('xlim'):
                inset.set_xlim(*kwargs.get('xlim'))
            else:
                inset.set_xlim(-750, 750)
            if meas[nr].data['Structure'] == 'Crosses' and kwargs.get('crosses_xlim'):
                inset.set_xlim(*kwargs.get('crosses_xlim'))

    plt.savefig("%s.pdf" % filename)

def plot_hloops_90(to_show=[57,155], filename='hloop-compare-90', **kwargs):
    """Compares +90deg with -90deg for (180deg Comparison)

    Args:
        to_show (TYPE, optional): DESCRIPTION. The default is [57,155].
        filename (TYPE, optional): DESCRIPTION. The default is
            'hloop-compare-90'.
        **kwargs (TYPE): mirror: bool, optional
                should we mirror the hloop? The default is False

    Returns:
        None.:
    """
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', 
                     palette='deep', latex=True)
    sns.set_palette(sns.color_palette("deep"))

    fig, axes = plt.subplots(2, 2, figsize=(16,12))
    for i, nr in enumerate(to_show):
        cur_ax = axes[i]
        ana.set_sns(size='talk', style='ticks', palette='Paired',
                         grid=True, latex=True)
        

        meas[nr] = ana.Hloop(nr)

        if not(kwargs.get('mirror')) and nr == 57:
            meas[nr].set_factor(-1)
            meas[nr].factor = 1


        # Plusses
        ax = cur_ax[0]
        meas[nr].plot_strayfield(ax, nolegend=True,
                                 show_plusses=False,
                                 show_crosses=False)

        ax.plot(meas[nr].up_fitted.B, meas[nr].up_fitted.Bx8, label='Up (fitted)')
        ax.plot(meas[nr].down_fitted.B, meas[nr].down_fitted.Bx8, label='Down (fitted)')

        # Set Limits (x and y Axis)
        if kwargs.get('xlim'):
            ax.set_xlim(*kwargs.get('xlim'))
        else:
            ax.set_xlim(-750, 750)

        ax.set_ylim(np.min([meas[nr].up_fitted.Bx8.min(),
                            meas[nr].down_fitted.Bx8.min()])-.05, 
                    np.max([meas[nr].up_fitted.Bx8.max(),
                            meas[nr].down_fitted.Bx8.max()])+.05)

        
        if nr == 57:
            ax.set_title('M57: Plusses ($90^\circ$)')
        else:
            ax.set_title('M155: Plusses ($-90^\circ$)')

        # Inset with Difference
        with sns.color_palette('bright'):
            if nr == 57 and not(kwargs.get('mirror')):
                bbox = (.11, .59, .34, .35)
            else:
                bbox = (.11, .12, .34, .35)
            inset = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=bbox,
                           bbox_transform=ax.transAxes)
            max_b = meas[nr].up.B.max()
            B_ext, B_stray = meas[nr].get_downminusup_strayfield(
                                            fitted_data=True)
            inset.plot([-max_b, max_b], [0, 0], '--', color='orange', linewidth=.75)
            inset.plot(B_ext, B_stray)
            inset.set_xlim(-750, 750)
            inset.set_title("Difference (fitted)")

        ax.legend(loc='upper right')#, ncol=2)

        # Crosses
        ax = cur_ax[1]
        meas[nr].plot_strayfield(ax, nolegend=True,
                                 show_plusses=False,
                                 show_crosses=False)
        ax.plot(meas[nr].up_fitted.B, 
                meas[nr].up_fitted.Bx9, label='Up (fitted)')
        ax.plot(meas[nr].down_fitted.B, 
                meas[nr].down_fitted.Bx9, label='Down (fitted)')

        # Set Limits (x and y Axis)
        if kwargs.get('xlim'):
            ax.set_xlim(*kwargs.get('xlim'))
        else:
            ax.set_xlim(-750, 750)
        
        ax.set_ylim(np.min([meas[nr].up_fitted.Bx9.min(),
                            meas[nr].down_fitted.Bx9.min()])-.05, 
                    np.max([meas[nr].up_fitted.Bx9.max(),
                            meas[nr].down_fitted.Bx9.max()])+.05)

        if nr == 57:
            ax.set_title('M57: Crosses ($90^\circ$)')
        else:
            ax.set_title('M155: Crosses ($-90^\circ$)')

        # Inset with Difference
        with sns.color_palette('bright'):
            if nr == 57 and kwargs.get('mirror'):
                bbox = (.11, .12, .34, .35)
            else:
                bbox = (.11, .59, .34, .35)
            inset2 = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=bbox,
                           bbox_transform=ax.transAxes)
            f_up = scipy.interpolate.interp1d(meas[nr].up_fitted.B,
                                              meas[nr].up_fitted.Bx9)
            f_down = scipy.interpolate.interp1d(meas[nr].down_fitted.B,
                                                meas[nr].down_fitted.Bx9)
            B = np.linspace(meas[nr].up.B.min(), meas[nr].up.B.max(), int(1e5))
            downminusup = f_down(B) - f_up(B)
            inset2.plot([-max_b, max_b], [0, 0], '--', 
                        color='orange', linewidth=.75)
            inset2.plot(B, downminusup, color='green')
            inset2.set_xlim(-750, 750)
            inset2.set_title("Difference (fitted)")
            if nr == 57:
                inset.set_yticklabels(['', '$0.0$', '', '$0.5$'])
                inset2.set_yticklabels(['', '$0.0$', '', '$0.5$'])

        ax.legend(loc='upper right')#, ncol=2)

    plt.savefig("%s.pdf" % filename)


def plot_hloops_90_nofit(to_show=[57,155], filename='hloop-compare-90', **kwargs):
    """Compares +90deg with -90deg for (180deg Comparison) Using not fitted data

    Args:
        to_show (TYPE, optional): DESCRIPTION. The default is [57,155].
        filename (TYPE, optional): DESCRIPTION. The default is
            'hloop-compare-90'.
        **kwargs (TYPE): mirror: bool, optional
                should we mirror the hloop? The default is False

    Returns:
        None.:
    """
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', 
                     palette='deep', latex=True)
    sns.set_palette(sns.color_palette("deep"))

    fig, axes = plt.subplots(2, 2, figsize=(16,12))
    for i, nr in enumerate(to_show):
        cur_ax = axes[i]
        ana.set_sns(size='talk', style='ticks', palette='Paired',
                         grid=True, latex=True)
        

        meas[nr] = ana.Hloop(nr)

        if not(kwargs.get('mirror')) and nr == 57:
            meas[nr].set_factor(-1)
            meas[nr].factor = 1


        # Plusses
        ax = cur_ax[0]
        meas[nr].plot_strayfield(ax, nolegend=True,
                                 show_plusses=False,
                                 show_crosses=False)

        ax.plot(meas[nr].up.B, meas[nr].up.Bx8, label='Up')
        ax.plot(meas[nr].down.B, meas[nr].down.Bx8, label='Down')
        ax.plot(meas[nr].up.B, meas[nr].up.Bx13, label='Up (Empty)')
        ax.plot(meas[nr].down.B, meas[nr].down.Bx13, label='Down (Empty)')

        # Set Limits (x and y Axis)
        if kwargs.get('xlim'):
            ax.set_xlim(*kwargs.get('xlim'))
        else:
            ax.set_xlim(-1000, 1000)

        ax.set_ylim(np.min([meas[nr].up.Bx8.min(),
                            meas[nr].down.Bx8.min()])-.05, 
                    np.max([meas[nr].up.Bx8.max(),
                            meas[nr].down.Bx8.max()])+.05)

        
        if nr == 57:
            ax.set_title('M57: Plusses ($90^\circ$)')
        else:
            ax.set_title('M155: Plusses ($-90^\circ$)')

        # Inset with Difference
        with sns.color_palette('bright'):
            if nr == 57 and not(kwargs.get('mirror')):
                bbox = (.11, .59, .34, .35)
            else:
                bbox = (.59, .12, .34, .35)
            inset = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=bbox,
                           bbox_transform=ax.transAxes)
            max_b = meas[nr].up.B.max()
            B_ext, B_stray = meas[nr].get_downminusup_strayfield()
            inset.plot([-max_b, max_b], [0, 0], '--', color='orange', linewidth=.75)
            inset.plot(B_ext, B_stray)
            inset.set_xlim(-1000, 1000)
            inset.set_title("Difference")


        # Crosses
        ax = cur_ax[1]
        meas[nr].plot_strayfield(ax, nolegend=True,
                                 show_plusses=False,
                                 show_crosses=False)
        ax.plot(meas[nr].up.B, meas[nr].up.Bx9, label='Up')
        ax.plot(meas[nr].down.B, meas[nr].down.Bx9, label='Down')
        ax.plot(meas[nr].up.B, meas[nr].up.Bx13, label='Up (Empty)')
        ax.plot(meas[nr].down.B, meas[nr].down.Bx13, label='Down (Empty)')

        # Set Limits (x and y Axis)
        if kwargs.get('xlim'):
            ax.set_xlim(*kwargs.get('xlim'))
        else:
            ax.set_xlim(-1000, 1000)
        
        ax.set_ylim(np.min([meas[nr].up.Bx9.min(),
                            meas[nr].down.Bx9.min()])-.05, 
                    np.max([meas[nr].up.Bx9.max(),
                            meas[nr].down.Bx9.max()])+.05)

        if nr == 57:
            ax.set_title('M57: Crosses ($90^\circ$)')
        else:
            ax.set_title('M155: Crosses ($-90^\circ$)')

        # Inset with Difference
        with sns.color_palette('bright'):
            if nr == 57 and kwargs.get('mirror'):
                bbox = (.11, .12, .34, .35)
            else:
                bbox = (.11, .59, .34, .35)
            inset2 = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=bbox,
                           bbox_transform=ax.transAxes)
            f_up = scipy.interpolate.interp1d(meas[nr].up.B,
                                              meas[nr].up.Bx9)
            f_down = scipy.interpolate.interp1d(meas[nr].down.B,
                                                meas[nr].down.Bx9)
            B = np.linspace(meas[nr].up.B.min(), meas[nr].up.B.max(), int(1e5))
            downminusup = f_down(B) - f_up(B)
            inset2.plot([-max_b, max_b], [0, 0], '--', 
                        color='orange', linewidth=.75)
            inset2.plot(B, downminusup, color='green')
            inset2.set_xlim(-1000, 1000)
            inset2.set_title("Difference")
            if nr == 57:
                inset.set_yticklabels(['', '$0.0$', '', '$0.5$'])
                inset2.set_yticklabels(['', '$0.0$', '', '$0.5$'])

        #if nr == 57 and not kwargs.get('mirror'):
        #    ax.legend(loc='upper left')#, ncol=2)
        if not (nr == 57):
            ax.legend(loc='upper right')#, ncol=2)

    plt.savefig("%s.pdf" % filename)

    
def plot_hloops2(to_show=a[85]+a[100], filename='hloop-compare-3', **kwargs):
    """Outputs hloop-compare-3.pdf (not used anymore)

    Args:
        to_show (TYPE, optional): DESCRIPTION. The default is a[85]+a[100].
        filename (TYPE, optional): DESCRIPTION. The default is
            'hloop-compare-3'.
        **kwargs (TYPE): DESCRIPTION.

    Returns:
        None.:
    """
    fig, axes = plt.subplots(2, 2, figsize=(16,12))
    for i, nr in enumerate(to_show):
        ax = axes[i//2][i%2]
        ana.set_sns(size='talk', style='ticks',
                         grid=True, latex=True)
        meas[nr] = ana.Hloop(nr)
        meas[nr].plot_strayfield(ax)
        ax.set_xlim(-750, 750)
        if nr == 58:
            ax.set_ylim(meas[nr].down_fitted.Bx8.max(), meas[nr].up_fitted.Bx8.min() )
        with sns.color_palette('deep'):
            ana.set_sns(size='talk', style='ticks',
                             grid=True, latex=True)
            if nr in [58, 59]:
                bbox = (.13, .02, .35, .35)
            else:
                bbox = (.65, .02, .35, .35)
            inset = inset_axes(ax, width='100%', height='90%', 
                           bbox_to_anchor=bbox,
                           bbox_transform=ax.transAxes)
            max_b = meas[nr].up.B.max()
            inset.plot([-max_b, max_b], [0, 0], 'r--', linewidth=.75)
            B_ext, B_stray = meas[nr].get_downminusup_strayfield()
            inset.plot(B_ext, B_stray)
            inset.set_xlim(-750, 750)
            if not(nr in [58, 59]):
                inset.set_ylabel("$\Delta B_z\\;[\\mathrm{mT}]$")
                inset.set_title("Difference")
            inset.set_xticklabels([])
            inset.set_xticks([])

    plt.savefig("%s.pdf" % filename)


def plot_hloops3(to_show=[139, 140],
                 filename='hloop-repeat',
                 xlim=(-350, 350),
                 ylim=None,
                 inset_xlim=(-30, 30),
                 inset_ylim=(0.15, 1.25)
                 ):
    """
        Compares two measurements at the same Angle (repeated measurements).

    Args:
        to_show (TYPE, optional): DESCRIPTION. The default is [139,140].
        filename (TYPE, optional): DESCRIPTION. The default is 'hloop-repeat'.
        xlim (TYPE, optional): DESCRIPTION. The default is (-350, 350).
        ylim:
        inset_xlim (TYPE, optional): DESCRIPTION. The default is (-30, 30).
        inset_ylim (TYPE, optional): DESCRIPTION. The default is (.15, 1.25).

    Returns:
        None.:
    """
    ana.set_sns(size='talk', style='ticks', palette='Paired',
                     grid=True, latex=True)
    fig, ax = plt.subplots(1, 1, figsize=(16,12))
    bmin, bmax = [], []
    for i, nr in enumerate(to_show):
        #ax = axes[i//2][i%2]
        meas[nr] = ana.Hloop(nr)
        meas[nr].plot_strayfield(ax, nolegend=True)
        ax.set_xlim(*xlim)
        bmin1, bmax1 = meas[nr].get_bhminmax()
        bmin.append(bmin1)
        bmax.append(bmax1)

    if ylim:
        ax.set_ylim(*ylim)
    else:
        ax.set_ylim(np.min(bmin)-.05, np.max(bmax)+.05)
    ax.set_title("M%s/%s: %s ($%s^\\circ$)" % (to_show[0], to_show[1],
                                               meas[nr].data['Structure'].replace('_', '\_'),
                                               meas[nr].data['Angle']))
    ax.legend(["M%d: Up" % to_show[0], "M%d: Down" % to_show[0],
               "M%d: Up" % to_show[1], "M%d: Down" % to_show[1],])
    y1, y2 = inset_ylim[0], inset_ylim[1]
    x1, x2 = inset_xlim[0], inset_xlim[1]
    ax.fill([x1, x1, x2, x2], [y1, y2, y2, y1], 'blue', alpha=.1)

    with sns.color_palette('bright'):
        bbox = (.65, .055, .35, .3)
        inset = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=bbox,
                       bbox_transform=ax.transAxes)
        max_b = meas[nr].up.B.max()
        for nr in to_show:
            B_ext, B_stray = meas[nr].get_downminusup_strayfield()
            inset.plot(B_ext, B_stray)
            inset.plot([-max_b, max_b], [0, 0], '--', linewidth=.75)
        inset.set_xlim(*xlim)
        inset.set_ylabel("$\Delta B_z\\;[\\mathrm{mT}]$")
        inset.set_title("Difference")

    with sns.color_palette('Paired'):
        bbox = (.07, .45, .35, .35)
        inset2 = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=bbox,
                       bbox_transform=ax.transAxes)
        for nr in to_show:
            meas[nr].plot_strayfield(inset2, nolegend=True)
        inset2.set_xlim(*inset_xlim)
        inset2.set_ylim(*inset_ylim)
        inset2.set_title("")
        inset2.set_ylabel('')

    with sns.color_palette('Paired'):
        bbox = (.65, .43, .35, .3)
        inset3 = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=bbox,
                       bbox_transform=ax.transAxes)
        plot_hloop_gradient3(inset3, nr=to_show, limit=inset_xlim[1],)
        #inset3.set_xticklabels([''])
        inset3.set_xlim(*inset_xlim)
        inset3.set_xlabel('')
        inset3.legend_.remove()

    plt.savefig("%s.pdf" % filename)

def plot_hloops_compare_90(to_show=[414, 415],
                 structure='plusses',
                 filename='hloop-repeat-414',
                 xlim=(-750, 750),
                 ylim=(-.36, .76),
                 inset_xlim=(-225, 225),
                 inset_ylim=(-.35, .75),
                 legend_loc='upper right',
                 nograd=False
                 ):
    """
        Compares multiple measurements at 90 deg (repeated measurements).

    Args:
        to_show (TYPE, optional): DESCRIPTION. The default is [414,415].
        structure:
        filename (TYPE, optional): DESCRIPTION. The default is
            'hloop-repeat-414'.
        xlim (TYPE, optional): DESCRIPTION. The default is (-750, 750).
        ylim:
        inset_xlim (TYPE, optional): DESCRIPTION. The default is (-100, 100).
        inset_ylim (TYPE, optional): DESCRIPTION. The default is (-1.25, .75).
        legend_loc:
        nograd:

    Returns:
        None.:
    """
    ana.set_sns(size='notebook', style='ticks', palette='Paired',
                     grid=True, latex=True)
    fig, ax = plt.subplots(1, 1, figsize=(16,12))
    legend = []
    m_numbers = str(to_show[0])
    if structure == 'plusses':
        column = 'Bx8'
    elif structure == 'crosses':
        column = 'Bx9'

    for i, nr in enumerate(to_show):
        #ax = axes[i//2][i%2]
        meas[nr] = ana.Hloop(nr) # Load Measurement
        meas[nr].remove_zero() # Remove Measurement Errors
        
        meas[nr].plot_strayfield(ax, nolegend=True,
                                 show_plusses=(structure == 'plusses'),
                                 show_crosses=(structure == 'crosses'))
        ax.set_xlim(*xlim)
        
        legend += ["M%d: Up" % nr, "M%d: Down" % nr]
        if i > 0:
            m_numbers += '/%d' % nr

    if ylim:
        ax.set_ylim(*ylim)

    ana.set_sns(size='talk', style='ticks', palette='Paired',
                     grid=True, latex=True)
    ax.set_title("M%s: %s ($%s^\\circ$)" % (m_numbers,
                                               structure.capitalize(),
                                               meas[nr].data['Angle']))
    
    # Draw Insets
    y1, y2 = inset_ylim[0], inset_ylim[1]
    x1, x2 = inset_xlim[0], inset_xlim[1]
    ax.fill([x1, x1, x2, x2], [y1, y2, y2, y1], 'blue', alpha=.1)

    ana.set_sns(size='notebook', style='ticks', palette='Paired',
                     grid=True, latex=True)
    with sns.color_palette('bright'):
        bbox = (.7, .06, .3, .3)
        inset = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=bbox,
                       bbox_transform=ax.transAxes)
        max_b = meas[nr].up.B.max()
        for i, nr in enumerate(to_show):
            if structure == 'plusses':
                B_ext, B_stray = meas[nr].get_downminusup_strayfield(fitted_data=True)
            else:
                up = meas[nr].up_fitted
                down = meas[nr].down_fitted
                f_up = scipy.interpolate.interp1d(up.B, up.Bx9)
                f_down = scipy.interpolate.interp1d(down.B, down.Bx9)
                B_ext = np.linspace(up.B.min(), up.B.max(), int(1e5))
                B_stray = f_down(B_ext) - f_up(B_ext)
            if i == 3:
                inset.plot(B_ext, B_stray, color='orange')
            else:
                inset.plot(B_ext, B_stray)
            if i == 0:
                inset.plot([-max_b, max_b], [0, 0], '--', linewidth=.75)


        inset.set_xlim(*xlim)
        inset.set_ylabel("$\Delta B_z\\;[\\mathrm{mT}]$")
        inset.set_title("Difference")

    with sns.color_palette('Paired'):
        bbox = (.05, .05, .35, .35)
        inset2 = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=bbox,
                       bbox_transform=ax.transAxes)
        for i, nr in enumerate(to_show):
            inset2.plot(meas[nr].up_fitted.B, 
                        meas[nr].up_fitted[column])
            inset2.plot(meas[nr].down_fitted.B, 
                        meas[nr].down_fitted[column])
        inset2.set_xlim(*inset_xlim)
        inset2.set_ylim(*inset_ylim)

    if not nograd:
        with sns.color_palette('Paired'):
            bbox = (.08, .67, .27, .3)
            inset3 = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=bbox,
                           bbox_transform=ax.transAxes)
            c = column.replace('B', 'V')
            plot_hloop_gradient3(inset3, to_show, limit=inset_xlim[1], column=c)
            inset3.set_xlim(*inset_xlim)
            inset3.set_xlabel('')
            inset3.legend_.remove()

    sns.set('notebook')
    ax.legend(legend, loc=legend_loc, ncol=int(len(to_show)/2))

    plt.savefig("%s.png" % filename)

def plot_hloops4(m=m, filename='hloop-parallel', figtitle="M57: $90^\\circ$ Parallel measurement", **kwargs):
    """Plots a single Measurement (default: 90deg parallel)

    Args:
        m (TYPE, optional): DESCRIPTION. The default is m.
        filename (TYPE, optional): DESCRIPTION. The default is 'hloop-parallel'.
        figtitle (TYPE, optional): DESCRIPTION. The default is "M57: $90^\circ$
            Parallel measurement".
        **kwargs (TYPE): DESCRIPTION.

    Returns:
        None.:
    """
    fig, ax = plt.subplots(1, 1, figsize=(16,12))
    ana.set_sns(size='talk', style='ticks', palette='Paired',
                     grid=True, latex=True)
    #m.set_factor(-1)
    #m.factor = 1
    
    m.plot_strayfield(ax, figtitle=figtitle,
                      show_crosses=False)
    m.up_fitted.Bx9 += .25
    m.down_fitted.Bx9 += .25
    ax.plot(m.up_fitted.B, m.up_fitted.Bx9, label='Crosses: Up (fitted)')
    ax.plot(m.down_fitted.B, m.down_fitted.Bx9, label='Crosses: Down (fitted)')
    ax.set_xlim(-750, 750)
    if kwargs.get('ylim'):
        ax.set_ylim(*kwargs.get('ylim'))
    else:
        ax.set_ylim(-.8,1.8)
    ax.legend(loc='best')
    
    with sns.color_palette('bright'):
        bbox = (.06, .46, .35, .23)
        inset = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=bbox,
                       bbox_transform=ax.transAxes)
        max_b = m.up.B.max()
        B_ext, B_stray = m.get_downminusup_strayfield()
        inset.plot([-max_b, max_b], [0, 0], '--', color='orange', linewidth=.75)
        inset.plot(B_ext, B_stray)
        inset.set_xlim(-750, 750)
        inset.set_title("Difference Plusses")



        bbox = (.06, .06, .35, .22)
        inset2 = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=bbox,
                       bbox_transform=ax.transAxes)
        f_up = scipy.interpolate.interp1d(m.up.B, m.up.Bx9)
        f_down = scipy.interpolate.interp1d(m.down.B, m.down.Bx9)
        B = np.linspace(m.up.B.min(), m.up.B.max(), int(1e5))
        downminusup = f_down(B) - f_up(B)
        inset2.plot([-max_b, max_b], [0, 0], '--', color='orange', linewidth=.75)
        inset2.plot(B, downminusup, color='green')
        inset2.set_xlim(-750, 750)
        inset2.set_title("Difference Crosses")
    
    plt.savefig("%s.pdf" % filename)


def plot_cubes_trees():
    """Plots difference between RAW data from Cubes and Trees (1st Generation)

    Returns:
        None.:
    """
    ana.set_sns(size='talk', style='ticks', palette='deep',
                     grid=True, latex=True)
    file_list = ['data/Data/%sdeg_%s' % (angle, struct) for
                 angle in [90, -90] for
                 struct in ['cubes', 'Trees']
                 ]
    
    fig, axes = plt.subplots(2, 2, figsize=(16,12))
    comp = {}
    for i, f in enumerate(file_list):
        ax = axes[i//2][i%2]
        load_files = ['%s_%s.dat' % (f, direction) for
                 direction in ['a', 'b']]
        comp[i] = ana.Hloop(0, file_list=load_files)
        comp[i].set_factor(1e6)
        
        ax.plot(comp[i].up.B, comp[i].up.Vx8, label='Up')
        ax.plot(comp[i].down.B, comp[i].down.Vx8, label='Down')
        
        ax.set_ylabel("$V_x [\\mathrm{\\mu V}]$")
        ax.set_xlabel("$\\mu_0 H_{ext}$ $[\\mathrm{mT}]$")
        bmin, bmax, vmin, vmax = comp[i].get_minmax()
        ax.set_xlim(bmin, bmax)
        
        if f.find('cubes') > 0:
            struct = 'Cubes'
        else:
            struct = "Trees"
        
        ax.set_title("%s ($%s^\\circ$)" % (struct, f[10:13].strip('d')))

        with sns.color_palette('bright'):
            if i%2 == 1:
                bbox = (.69, .7, .3, .3)
            else:
                bbox = (.12, .7, .29, .3)
            inset = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=bbox,
                           bbox_transform=ax.transAxes)
            max_b = m.up.B.max()
            B_ext, B_stray = comp[i].get_downminusup()
            inset.plot([-max_b, max_b], [0, 0], '--', color='orange', linewidth=.75)
            inset.plot(B_ext, B_stray)
            inset.set_xlim(bmin, bmax)
            #inset.set_title("Difference")

    
    ax.legend(loc='lower left')
    
    plt.savefig("compare-cubes-trees.pdf")


def plot_hloop_gradient(m=m, limit=50, filename='hloop-gradient'):
    """Plotting the gradient along the

    Args:
        m:
        limit:
        filename:

    Returns:
        None.:
    """
    ana.set_sns(default=True, grid=True,
            style='ticks',
            size='talk',
            palette='deep',
            latex=True,)

    grad1 = [np.divide(np.diff(m.up.Vx8), np.diff(m.up.Time)),
            np.divide(np.diff(m.up.Vx9), np.diff(m.up.Time))]
    grad12 = [np.divide(np.diff(m.down.Vx8), np.diff(m.down.Time)),
            np.divide(np.diff(m.down.Vx9), np.diff(m.down.Time))]

    fig, axes = plt.subplots(2,1, sharex=True)
    for i in range(2):
        ax = axes[i]
        g = grad1[i]
        g2 = grad12[i]
        
        if i == 0:
            add = 'Plusses'
        else:
            add = 'Crosses'

        ax.set_title('M57: Gradient (%s)' % add)
        x = m.up[:-1]
        ax.plot(x.B[x.B.abs() < limit], 
                g[x.B.abs() < limit]*1e6, 
                label='Up (%s)' % add)
        x = m.down[:-1]
        ax.plot(x.B[x.B.abs() < limit], 
                g2[x.B.abs() < limit]*1e6, 
                label='Down (%s)' % add)
        ax.set_ylabel('$dV_H/dt\; [\\mu\\mathrm{V/s}]$')
    ax.set_xlabel('$\\mu_0 H_{ext} [\\mathrm{mT}]$')
    
    plt.savefig('%s.pdf' % filename)


def plot_hloop_gradient2(m=m, limit=50, filename='hloop-gradient'):
    """Plotting the gradient along the

    Args:
        m:
        limit:
        filename:

    Returns:
        None.:
    """
    ana.set_sns(default=True, grid=True,
            style='ticks',
            size='talk',
            palette='deep',
            latex=True,)

    grad = [np.gradient(m.up.Vx8, np.diff(m.up.Time).mean()),
            np.gradient(m.down.Vx8, np.diff(m.down.Time).mean())]

    fig, ax = plt.subplots()
    ax.set_title('M%s: Gradient (%s)' % (m.measurement_number,
                                         m.data['Structure']))
    for i in range(2):
        g = grad[i]
        
        if i == 0:
            x = m.up
            add = 'Up'
        else:
            x = m.down
            add = 'Down'

        ax.plot(x.B[x.B.abs() < limit], 
                g[x.B.abs() < limit]*1e6, 
                label='%s' % add)
    ax.set_ylabel('$dV_H/dt\; [\\mu\\mathrm{V/s}]$')
    ax.legend(loc='best')
    ax.set_xlabel('$\\mu_0 H_{ext} [\\mathrm{mT}]$')
    
    plt.savefig('%s.pdf' % filename)


def plot_hloop_gradient3(ax, to_show=[139,140], limit=50, column='Vx8'):
    """Plotting the gradient along the

    Args:
        ax:
        to_show:
        limit:
        column:

    Returns:
        None.:
    """
    #ana.set_sns(default=True, grid=True,
    #        style='ticks',
    #        size='talk',
    #        palette='Paired',
    #        latex=True,)
    
    limit = np.abs(limit)

    ax.set_title('Gradient')
    for nr in to_show:
        m = meas[nr]
        c = column
        grad = [np.divide(np.diff(m.up[c]), np.diff(m.up.Time)),
                np.divide(np.diff(m.down[c]), np.diff(m.down.Time))]
        for i in range(2):
            g = grad[i]
    
            if i == 0:
                x = m.up[:-1]
                direction = 'Up'
            else:
                x = m.down[:-1]
                direction = 'Down'
    
            ax.plot(x.B[x.B.abs() < limit], 
                    g[x.B.abs() < limit]*1e6, 
                    label='M%s: %s' % (m.measurement_number, direction))

    #ax.set_xlim(-limit, limit)
    ax.set_ylabel('$dV_H/dt\; [\\mu\\mathrm{V/s}]$')
    ax.legend(loc='best')
    ax.set_xlabel('$\\mu_0 H_{ext} [\\mathrm{mT}]$')

def plot_hloop_temp(m=m):
    """Plots the Temperature of a Hloop Measurement.

    Args:
        m:

    Returns:
        None.:
    """

    ana.set_sns(default=True, grid=True,
            style='ticks',
            size='talk',
            palette='deep',
            latex=True,)
    
    fig, ax = plt.subplots()
    ax.set_title('M%s: Sample Temperature' % m.measurement_number)
    
    ax.plot(m.up.B, (m.up['Sample Temp']), '-', label='Up')
    ax.plot(m.down.B, (m.down['Sample Temp']), '-', label='Down')

    ax.set_xlabel('$\\mu_0 H_{ext} [\\mathrm{mT}]$')
    ax.set_ylabel('Temperature $[\\mathrm{mK}]$')
    ax.legend(loc='best')
    
    plt.savefig('hloop-90-temp.pdf')


#### Plot Static Fields
def plot_static_fields():
    """Plot the Signal Analyzer (SA) Data for static fields (not sweeping)

    Returns:
        None.:
    """
    tmp = {
           'Plusses (25 mT)': 360,
           'Plusses (-25 mT)': 361,
           'Plusses (-9.4 mT)': 282,
           'Crosses (-9.4 mT)': 283,
           'Plusses (0 T)': 281,
           'Crosses (0 T)': 280,
           'Empty (0 T)': 310,
           #'Crosses (250 mT)': 315,
           }
    lofm = {}
    for i, j in tmp.items():
        lofm.update({j: ['%s' % i, {}]})
    
    ana.set_sns(default=True, grid=True,
            style='ticks',
            size='talk',
            palette='Paired',
            latex=True,)

    fig, ax = eva.plot(lofm, 
                       plot_settings=dict(
                           title='($90^\\circ$) Static Field',
                           xlim=(2e-2, 5e0), 
                           ylim=(1e-7, 1e-3),
                           ),
                        f_settings=dict(
                            ymin=5e-5),
                        f2_settings=dict(disable=True),
                       )

    #ax = plt.gca()
    with sns.color_palette('deep'):
        inset = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=(.25, .58, .45, .4),
                           bbox_transform=ax.transAxes)
        m.plot_strayfield(inset, 'Strayfield Plusses', nolegend=True)
        inset.legend(['Up',#' ($-M_S \\rightarrow +M_S$)', 
                      'Down']) #' ($+M_S \\rightarrow -M_S$)'])
        inset.grid(b=True, alpha=.4)
        inset.set_xlim(-50, 50)
        inset.set_ylim(-.65, .45)
    
        a = lambda x: m.down.Bx8.iloc[(m.down.B + x).abs().idxmin()]
        b = lambda x: m.up.Bx8.iloc[(m.up.B + x).abs().idxmin()]
        inset.plot((-25, -25), (a(25), a(25)), 'o', color='#000099', alpha=.6)
        inset.plot([+25, 25], [b(-25), b(-25)], 'o', color='#9999FF', alpha=.6)
        inset.plot([-9.4, -9.4], [a(9.4), a(9.4)], 'o', color='green', alpha=.6)
        inset.plot([0], [a(0)], 'o', color='#FF3333', alpha=.8)
        
        #ana.set_relative_yticks(inset)
        inset.set_xticks(np.arange(-50,51,25))

    plt.savefig('static-field-w-inset.pdf')

#### Sweeping Field
def first_sweeps(add=False):
    """First field sweeps (plus minus 50/75/100/etc.)

    Args:
        add:

    Returns:
        vacant-sweeps.pdf:
    """
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', latex=True,
                     palette='deep')
    
    lofm = {}
    to_show = {
        #382: [(-25,25), 'Plusses', 5, {}],
        362: [(-50,50), 'Plusses', 2, {}],
        363: [(-75,75), 'Plusses', 2, {}],
        364: [(-100,100), 'Plusses', 2, {}],
        366: [(-125,125), 'Plusses', 2, {}],
        365: [(-150,150), 'Plusses', 2, {}],
        #352: [("-M_s \\rightarrow -25",25), 'Plusses', .1],
    }
    if add:
        to_show.update({
                336: [(-500,500), 'Plusses', 9.4, {}],
                331: [('\\mathrm{C}\\,{%s}' % -100,100), 'Crosses', 9.4, {'linestyle': '--'}],
                332: [('\\mathrm{C}\\,{%s}' % -300,300), 'Crosses', 9.4, {'linestyle': '--'}],
                333: [('\\mathrm{C}\\,{%s}' % -750,750), 'Crosses', 9.4, {'linestyle': '--'}],
                })
    
    for nr, content in to_show.items():
        lofm[nr] = ["$%s \\rightarrow %s\\;\\mathrm{mT}$" % (
                    content[0][0],
                    content[0][1],
                    ), content[3]]

    fig, ax = eva.plot(lofm,
           #fit_range=(2e-2, 9e-1),
           #show_fit=True,
             plot_settings=dict(
                 title='($90^\\circ$) Field Sweeps (Inside the Hysteresis)',
                 xlim=(1e-2, 1e0),
                 ylim=(4e-7, 7e-2)),
             f_settings=dict(
                 xmin=5e-2,
                 ymin=1e-5),
             f2_settings=dict(
                 xmin=2e-2,
                 ymin=1e-2,
                 ),
             )

    # Inset with Strayfield
    if not add:
        with sns.color_palette('deep'):
            inset = inset_axes(ax, width='100%', height='100%', 
                               bbox_to_anchor=(.74, .45, .25, .25),
                               bbox_transform=ax.transAxes)
            # Plotting Lines for each measurement
            y1, y2 = -1, 1
            for nr, content in to_show.items():
                x1 = content[0][1]
                inset.plot([x1,x1,-x1,-x1], [y1,y2,y2,y1])
    
            m.plot_strayfield(inset, 'Strayfield Plusses', 
                              show_plusses=False,
                              show_crosses=False,
                              nolegend=True)
    
            inset.plot(m.up_fitted.B, m.up_fitted.Bx8, '-',
                       color=(76/255, 114/255, 176/255),
                       linewidth=3, label='Up')
            inset.plot(m.down_fitted.B, m.down_fitted.Bx8, 'r-', 
                       color=(221/255, 132/255, 82/255),
                       linewidth=1.5, label='Down')
    
            inset.legend(['Up',# ($-M_S \\rightarrow +M_S$)', 
                          'Down'])# ($+M_S \\rightarrow -M_S$)'])
            inset.grid(b=True, alpha=.4)
            inset.set_xlim(-200, 200)
            inset.set_ylim(-.65, .45)
            inset.set_xticks([-200+50*_ for _ in range(9)])
            inset.set_xticks([-175+50*_ for _ in range(8)], minor=True)
            inset.set_yticks([-0.25+.5*_ for _ in range(2)], minor=True)
            inset.grid(b=True, which='minor', color='#cccccc', linestyle='-.', alpha=.3)
    
            # X-Ticks (labels)
            xt_labels = []
            for i in [-200+50*_ for _ in range(9)]:
                if i%100 == 0:
                    xt_labels += ['$%s$' % i]
                else:
                    xt_labels += ['']
            inset.set_xticklabels(xt_labels)


    # Inset showing fitted data
    with sns.color_palette("deep"):
        inset2 = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=(.44, .75, .3, .25),
                           bbox_transform=ax.transAxes)
        inset3 = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=(.09, .09, .3, .25),
                           bbox_transform=ax.transAxes)

        for nr, content in to_show.items():
            intercept, slope = eva[nr].fit(fit_range=(2e-2, 9e-1))
            voltage = content[0][1]

            inset2.plot(voltage, 10**intercept, 'o')
            inset3.plot(voltage, slope, 'o')

        inset2.set_xlabel('End field [$\mu_0 \mathrm{H_{ext}}$]')
        inset2.set_ylabel('$S_{V_H} (f=1\\;$Hz$)$')
        inset2.set_yscale('log')
        inset2.set_yticks([8e-7, 9e-7, 1e-6, 2e-6])

        inset3.set_xlabel('End field [$\mu_0 \mathrm{H_{ext}}$]')
        inset3.set_ylabel('$\\alpha$')

    plus = ''
    if add:
        plus = '-enhanced'
    plt.savefig('vacant-sweeps%s.pdf' % plus)

def compare_voltages():
    """Compare different applied Voltages.

    Returns:
        compare-voltages.pdf:
    """
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', latex=True,
                     palette='deep')
    
    lofm = {}
    to_show = {}
    for i in range(1,7):
        to_show[i+377] = i
    
    for nr, content in to_show.items():
        lofm[nr] = ["$%s\\;\\mathrm{V}$" % (
                    content
                    ),{}]

    fig, ax = eva.plot(lofm,
             #fit_range=(2e-2, 7e-1),
             #show_fit=True,
             plot_settings=dict(
                 title='($90^\\circ$) Field Sweeps (Different Voltages)',
                 xlim=(1e-2, 1e0),
                 ylim=(4e-7, 7e-2)),
             f_settings=dict(disable=True,
                 xmin=5e-2,
                 ymin=1e-5),
             f2_settings=dict(
                 xmin=1.5e-1,
                 ymin=2e-3,
                 ),
             )

    # Inset with Strayfield
    with sns.color_palette('deep'):
        inset = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=(.07, .38, .26, .26),
                           bbox_transform=ax.transAxes)
        m.plot_strayfield(inset, 'Strayfield Plusses', 
                          nolegend=True,)
        inset.legend(['Up',# ($-M_S \\rightarrow +M_S$)', 
                      'Down'])# ($+M_S \\rightarrow -M_S$)'])
        inset.grid(b=True, alpha=.4)
        inset.set_xlim(-50, 50)
        inset.set_ylim(-.65, .45)
        inset.set_xticks([-50+25*_ for _ in range(5)])
        #inset.set_xticks([-45+10*_ for _ in range(10)], minor=True)
        inset.grid(b=True, which='minor', color='#cccccc', 
                   linestyle='-.', alpha=.3)
        #inset.set_xlabel('')
        inset.set_ylabel('')

        y1, y2 = -1, 2
        inset.fill([-25, -25, 25, 25], [y1, y2, y2, y1], 'blue', alpha=.1)
        inset.annotate("", xy=(25, -.35), xytext=(-25, -.2),
                     arrowprops=dict(arrowstyle="->", color='blue'))

    # Inset showing fitted data
    with sns.color_palette("deep"):
        inset2 = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=(.54, .75, .3, .25),
                           bbox_transform=ax.transAxes)
        inset3 = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=(.3, .09, .3, .25),
                           bbox_transform=ax.transAxes)
    
        for nr, content in to_show.items():
            intercept, slope = eva[nr].fit(fit_range=(2e-2, 7e-1))
            voltage = content
    
            inset2.plot(voltage, 10**intercept, 'o')
            inset3.plot(voltage, slope, 'o')
    
        inset2.set_xlabel('Voltage [$\mathrm{V}$]')
        inset2.set_ylabel('$S_{V_H} (f=1\\;$Hz$)$')
        inset2.set_yscale('log')

        inset3.set_xlabel('Voltage [$\mathrm{V}$]')
        inset3.set_ylabel('$\\alpha$')

    plt.savefig('compare-voltages.pdf')



def compare_sweeprates():
    """Compare different Sweeprates, fits the data and

    Returns:
        None.:
    """
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', latex=True,
                     palette='deep')

    lofm = {}
    to_show = {
        382: [("-M_s \\rightarrow -25",25), 'Plusses', 5],
        354: [("-M_s \\rightarrow -25",25), 'Plusses', 2],
        351: [("-M_s \\rightarrow -25",25), 'Plusses', 1],
        355: [("-M_s \\rightarrow -25",25), 'Plusses', .5],
        353: [("-M_s \\rightarrow -25",25), 'Plusses', .25],
        352: [("-M_s \\rightarrow -25",25), 'Plusses', .1],
    }

    for nr, content in to_show.items():
        lofm[nr] = ["$%s\\;\\frac{\\mathrm{mT}}{\\mathrm{min}}$" % (
                    content[2],
                    ),{}]

    fig, ax = eva.plot(lofm,
           #fit_range=(2e-2, 5e-1),
           #show_fit=True,
             plot_settings=dict(
                 title='($90^\\circ$) Field Sweeps (Compare different Sweep Rates)',
                 xlim=(1e-2, 1.6e0),
                 ylim=(4e-7, 5e-2)),
             f_settings=dict(
                 xmin=5e-2,
                 ymin=1e-5),
             f2_settings=dict(
                 xmin=1.5e-1,
                 ),
             )
    
    ax = plt.gca()
    # Inset with Strayfield
    with sns.color_palette('deep'):
        inset = inset_axes(ax, width='100%', height='90%', 
                           bbox_to_anchor=(.1, .06, .3, .33),
                           bbox_transform=ax.transAxes)
        m.plot_strayfield(inset, 'Strayfield Plusses', 
                          nolegend=True,)
        inset.legend(['Up',# ($-M_S \\rightarrow +M_S$)', 
                      'Down'])# ($+M_S \\rightarrow -M_S$)'])
        inset.grid(b=True, alpha=.4)
        inset.set_xlim(-50, 50)
        inset.set_ylim(-.65, .45)
        inset.set_xticks([-50+25*_ for _ in range(5)])
    
        y1, y2 = -1, 2
        inset.fill([-25, -25, 25, 25], [y1, y2, y2, y1], 'blue', alpha=.1)
        inset.annotate("", xy=(25, -.35), xytext=(-25, -.2),
                     arrowprops=dict(arrowstyle="->", color='blue'))


    # Inset showing fitted data
    with sns.color_palette("deep"):
        inset2 = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=(.5, .75, .3, .25),
                           bbox_transform=ax.transAxes)
    
        for nr, content in to_show.items():
            intercept, slope = eva[nr].fit(fit_range=(2e-2, 5e-1))
            sweep_rate = content[2]
    
            inset2.plot(sweep_rate, 10**intercept, 'o')
    
        inset2.set_xlabel('Sweep Rate $\\left[\\frac{\\mathrm{mT}}{\\mathrm{min}}\\right]$')
        inset2.set_ylabel('$S_{V_H} (f=1\\;$Hz$)$')
        inset2.set_yscale('log')
        
    # Only save if necessary
    plt.savefig('sweeprate-effect.pdf')

def fast_sweeprate(show_numbers=[320, 325, 323, 329,], xlim=None, 
                   filename='FastSR-1', pos2=False, 
                   title='($90^\circ$) Field sweeps ($\\Delta B \\geq 1\\;\\mathrm{T}$)'):
    """anas Fast Sweeps over large sweep ranges (1T)

    Args:
        show_numbers:
        xlim:
        filename (TYPE, optional): DESCRIPTION. The default is 'FastSR-1'.
        pos2:
        title:

    Returns:
        None.:
    """
    to_show = {
        320: [(2,1), 'Empty', 9.4],
        321: [(2,1), 'Empty', 4.7],
        325: [(2,1), 'Crosses', 9.4],
        326: [(2,1), 'Crosses', 4.7],
        323: [(1,-1), 'Empty', 9.4],
        324: [(1,-1), 'Empty', 4.7],
        329: [(1,-1), 'Crosses', 9.4],
        322: [(.5,-.5), 'Empty', 9.4],
        327: [(.5,-.5), 'Crosses', 9.4],
        328: [(.5,-.5), 'Crosses', 4.7],
        336: [(.5,-.5), 'Plusses', 9.4],
        333: [(.75,-.75), 'Crosses', 9.4],
        332: [(.3,-.3), 'Crosses', 9.4],
        331: [(.1,-.1), 'Crosses', 9.4],
    }

    lofm = {}
    for nr, content in to_show.items():
        if content[2] == 4.7:
            continue
        if not(nr in show_numbers):
            continue
        lofm[nr] = '$%s \\rightarrow %s$ T %s ($%s \\frac{\\mathrm{mT}}{\\mathrm{min}}$)' % (
                    content[0][0],
                    content[0][1],
                    content[1],
                    content[2],
                    )
    
    ana.set_sns(default=True, grid=True, size='talk', style='ticks', 
                     latex=True, palette='Paired')
    fig, ax = plt.subplots(figsize=(16,12))
    for i,j in lofm.items():
        label = 'm%s: %s' % (i, j)
        if False:
            eva[i].plot(label=label, ax=ax, color='orange', 
                        dont_set_plot_settings=True)
        else:
            eva[i].plot(label=label, ax=ax, dont_set_plot_settings=True)

    eva[i]._set_plot_settings(xlim=(1e-2, 1.6e0), ylim=(1e-7, 5e-2), 
        title=title,
        grid=dict(which='minor', color='#ffff99', linestyle='--', alpha=.5))
    eva[i]._draw_oneoverf(ax, ymin=3e-4, xmin=2e-2, alpha=2, 
                          plot_style='b--', an_color='blue')
    #eva[i]._draw_oneoverf(ax, xmin=1e-2, ymin=1e-6)
    plt.grid(b=True, which='minor', color='#cccccc', linestyle='-.', alpha=.3)


    # Inset with Strayfield
    with sns.color_palette('deep'):
        if pos2:
            bbox = (.1, .1, .3, .25)
        else:
            bbox = (.32, .72, .3, .25)
        inset = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=bbox,
                           bbox_transform=ax.transAxes)

        m.plot_strayfield(inset, 'Strayfield Crosses', 
                          nolegend=True,
                          show_plusses=False)
        inset.grid(b=True, alpha=.4)
        if xlim:
            inset.set_xlim(*xlim)
        else:
            inset.set_xlim(-1000, 1000)
        inset.set_ylim(-1.45, -.8)

        if pos2:
            inset.set_xticks([-300+200*_ for _ in range(4)], minor=True)
            for color, x1 in [((202/255, 178/255, 214/255), 300), ((106/255, 61/255, 154/255), 100)]:
                y1, y2 = -2, 2
                inset.plot([x1, x1, -x1, -x1], [y1, y2, y2, y1], color=color)
        #inset.fill([-500, -500, 500, 500], [y1, y2, y2, y1], 'blue', alpha=.1)
        #inset.annotate("", xy=(25, .35), xytext=(-25, .2),
        #             arrowprops=dict(arrowstyle="->", color='blue'))
    
    plt.savefig('%s.pdf' % filename)


def sv_temp_effect():
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', latex=True,
                     palette='deep')

    lofm = {}
    to_show = {
        351: [("-M_s \\rightarrow -25",25), 'Plusses', 1, 30],
        355: [("-M_s \\rightarrow -25",25), 'Plusses', 0.5, 25],
        356: [("-M_s \\rightarrow -25",25), 'Plusses', 0.5, 20],
        357: [("-M_s \\rightarrow -25",25), 'Plusses', 0.5, 15],
        358: [("-M_s \\rightarrow -25",25), 'Plusses', 0.5, 10],
        359: [("-M_s \\rightarrow -25",25), 'Plusses', 0.5, 5],
    }

    for nr, content in to_show.items():
        lofm[nr] = ['$%s\\;\mathrm{K}$' % (
                    content[3],
                    ),{}]
        #eva[nr].Vx *= grad

    t = '($90^\\circ$) Field Sweeps (' + \
        'Temperature Effect; Sweeprate = $%s\\;{\\mathrm{mT}}/{\\mathrm{min}}$)' % (
                    content[2])

    fig, ax = eva.plot(lofm,
           #fit_range=(2e-2, 7e-1),
           #show_fit=True,
             plot_settings=dict(
                 title=t,
                 xlim=(1e-2, 1.6e0),
                 ylim=(6e-7, 5e-2)
             ),
             f_settings=dict(disable=True),
             f2_settings=dict(
                 xmin=7e-2
             )
        )

    # Inset with Strayfield
    with sns.color_palette('deep'):
        inset = inset_axes(ax, width='100%', height='90%', 
                           bbox_to_anchor=(.75, .4, .25, .25),
                           bbox_transform=ax.transAxes)
        m.plot_strayfield(inset, 'Strayfield Plusses', 
                          nolegend=True,)
        inset.legend(['Up', 'Down'], 
                     loc='upper right')
        inset.grid(b=True, alpha=.4)
        inset.set_xlim(-50, 50)
        inset.set_ylim(-.65, .45)
        inset.set_ylabel('')

        y1, y2 = -1, 2
        inset.fill([-25, -25, 25, 25], [y1, y2, y2, y1], 'blue', alpha=.1)
        inset.annotate("", xy=(25, -.35), xytext=(-25, -.2),
                     arrowprops=dict(arrowstyle="->", color='blue'))

    # Inset showing fitted data
    with sns.color_palette("deep"):
        inset2 = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=(.5, .75, .3, .25),
                           bbox_transform=ax.transAxes)
        inset3 = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=(.1, .09, .3, .3),
                           bbox_transform=ax.transAxes)

        for nr, content in to_show.items():
            intercept, slope = eva[nr].fit(fit_range=(2e-2, 7e-1))
            temp = content[3]
    
            inset2.plot(temp, 10**intercept, 'o')
            inset3.plot(temp, slope, 'o')

        inset2.set_xlabel('Temperature [$\mathrm{K}$]')
        inset2.set_ylabel('$S_{V_H} (f=1\\;$Hz$)$')
        inset2.set_yscale('log')
        inset2.set_xticks([5+10*_ for _ in range(3)], minor=True)

        inset3.set_xlabel('Temperature [$\mathrm{K}$]')
        inset3.set_ylabel('$\\alpha$')
        inset3.set_xticks([5+10*_ for _ in range(3)], minor=True)
    
    # Only save if necessary
    plt.savefig('sv-temp-effect.pdf')

def multiple_fspans():
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', latex=True,
                     palette='Paired')
    
    lofm = {}
    to_show = {
        340: [(25,-25), 'Empty', 0.46, {}],
        349: [("-25",25), 'Empty', 0.5, {}],
        338: [(25,-25), 'Plusses', 0.46, {}],
        342: [("+M_s \\rightarrow 25 \\rightarrow 8.3",-25), 'Plusses', +0.11, {}],
        343: [("-M_s \\rightarrow -25 \\rightarrow -8.3",25), 'Plusses', 0.11, {'color': 'red'}],
    }
    
    for nr, content in to_show.items():
        if content[2] == 9.4:
            continue
        lofm[nr] = ['$%s \\rightarrow %s$ mT %s ($%s \\frac{mT}{min}$)' % (
                    content[0][0],
                    content[0][1],
                    content[1],
                    content[2],
                    ),content[3]]
    
    eva.plot(lofm,
             plot_settings=dict(
                 title='($90^\\circ$) Field Sweeps ($B = \\pm 25 mT$)',
                 xlim=(6e-3, 1.6e0),
                 #ylim=()
             ),
             f_settings=dict(disable=True,
                 xmin=5e-2,
                 ymin=1e-5),
             f2_settings=dict(
                 xmin=1e-2,)
             )
    
    ax = plt.gca()
    with sns.color_palette('Dark2'):
        inset = inset_axes(ax, width='100%', height='90%', 
                           bbox_to_anchor=(.7, .44, .3, .3),
                           bbox_transform=ax.transAxes)
        m.plot_strayfield(inset, 'Strayfield Plusses', 
                          show_crosses=False,
                          nolegend=True)
        inset.legend(['Up', 'Down'])
        inset.grid(b=True, alpha=.4)
        s = 30
        inset.set_xlim(-s, s)
        inset.set_ylim(-.65, .45)
        s = 20
        inset.set_xticks(np.linspace(-s, s, 5))
        inset.set_xticks([-s-5+10*_ for _ in range(6)], minor=True)
    
        y1, y2 = -1, 2
        inset.fill([-25, -25, -8.3, -8.3], [y1, y2, y2, y1], 'red', alpha=.2)
        inset.fill([25, 25, 8.3, 8.3], [y1, y2, y2, y1], 'green', alpha=.2)
        inset.fill([8.3, 8.3, -8.3, -8.3], [y1, y2, y2, y1], 'blue', alpha=.05)
        #inset.plot([8.3, 8.3], [y1, y2], 'b-.', alpha=.8)
    
    # Only save if necessary
    plt.savefig('multiple-fspans.pdf')

def negative_sweeps():
    """Testing without file output.

    Returns:
        None.:
    """
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', latex=True,
                     palette='Paired')
    lofm = {}
    to_show = {
        340: [(25,-25), 'Empty', 0.46, {}],
        338: [(25,-25), 'Plusses', 0.46, {}],
        348: [("-M_s \\rightarrow 36.56",-291), 'Empty', 0.5, {}],
        347: [("-M_s \\rightarrow 36.56",-291), 'Plusses', 0.5,{}],
    }
    
    for nr, content in to_show.items():
        if content[2] == 9.4:
            continue
        options = content[3]
        lofm[nr] = ['$%s \\rightarrow %s$ mT %s ($%s \\frac{mT}{min}$)' % (
                    content[0][0],
                    content[0][1],
                    content[1],
                    content[2],
                    ),options]
    
    fig, ax = eva.plot(lofm,
             plot_settings=dict(
                 title='($90^\\circ$) Field Sweeps (Measurement Plan \#2)',
                 xlim=(6e-3, 1.6e0),
                 #ylim=()
             ),
             f_settings=dict(
                 xmin=6e-3,
                 ymin=1e-5))
    
    with sns.color_palette('muted'):
        inset = inset_axes(ax, width='100%', height='90%', 
                           bbox_to_anchor=(.28, .73, .29, .24),
                           bbox_transform=ax.transAxes)
        m.plot_strayfield(inset, 'Strayfield', nolegend=True)
        inset.legend(['Up ($-M_S \\rightarrow +M_S$)', 
                      'Down ($+M_S \\rightarrow -M_S$)'])
        inset.grid(b=True, alpha=.4)
        inset.set_xlim(-650, 50)
        inset.set_ylim(-.4, .6)
    
        y1, y2 = -1, 2
        inset.fill([-25, -25, 25, 25], [y1, y2, y2, y1], 'blue', alpha=.1)
        inset.fill([-291.13, -291.13, 36.56, 36.56], [y1, y2, y2, y1], 'green', alpha=.1)
        inset.fill([-611, -611, -443, -443], [y1, y2, y2, y1], 'orange', alpha=.1)
        inset.fill([-291, -291, -443, -443], [y1, y2, y2, y1], 'darkred', alpha=.1)

def measplan12():
    c1 = sns.color_palette("hls", 6)
    #sns.color_palette("Reds_r", 14)
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', latex=True,
                     palette='deep')
    sns.set_palette(c1)
    lofm = {}
    to_show = {
        383: [("+M_s \\rightarrow 25",-25), 'Plusses', +0.5, {}],
        384: [("-25",-75), 'Plusses', +0.5, {'color': 'orange', 'linestyle': '--'}],
    }
    
    for i in range(6):
        to_show.update(
            {
                (385+i): [("+M_s \\rightarrow %d" % (-(i*50+25)),(-(i*50+25) - 50)), 'Plusses', +0.5, {}],
            }
        )

    for nr, content in to_show.items():
        if content[2] == 9.4:
            continue
        options = content[3]
        lofm[nr] = ['$%s \\rightarrow %s\;\mathrm{mT}$' % (
                    content[0][0],
                    content[0][1],
                    ),options]
    
    fig, ax = eva.plot(lofm,
             plot_settings=dict(
                 title='($90^\\circ$) Field Sweeps (Plusses $0.5\;\mathrm{mT}/\mathrm{min}$)',
                 xlim=(1e-2, 1.6e0),
                 ylim=(3e-3, 6e-7)
             ),
             f_settings=dict(
                 xmin=1e-2,
                 ymin=3e-5),
             f2_settings=dict(#disable=True
                 xmin=2e-2,
                 plot_style='k-.',
                 an_color='k'
             ),
            )
    
    ax = plt.gca()
    with sns.color_palette(c1):
        inset = inset_axes(ax, width='100%', height='90%', 
                           bbox_to_anchor=(.4, .73, .29, .24),
                           bbox_transform=ax.transAxes)
        m.plot_strayfield(inset, 'Strayfield', nolegend=True)
        inset.legend(['Up ($-M_S \\rightarrow +M_S$)', 'Down ($+M_S \\rightarrow -M_S$)'])
        inset.grid(b=True, alpha=.4)
        inset.set_xlim(-650, 50)
        inset.set_ylim(-.6, .4)
    
        y1, y2 = -1, 2
        for j in [25] + [-25-50*i for i in range(5)]:# + [-300-50*i for i in range(5)] + [-575]:
            inset.fill([j, j, j-50, j-50], [y1, y2, y2, y1], alpha=.4)
        #for j in [-300-50*i for i in range(5)] + [-575]:
        #    inset.fill([j, j, j-50, j-50], [y1, y2, y2, y1], alpha=.4)
    ax.annotate('Without Saturation', (1.2e-2, 1e-3), color='orange',
                rotation=-55)
    ax.annotate('With Saturation', (1.01e-2, .8e-3), color='yellow', 
                rotation=-37)

    plt.savefig('measplan12-1.pdf')

def measplan12_2():
    c1 = sns.color_palette("hls", 7)
    #sns.color_palette("Reds_r", 14)
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', latex=True,
                     palette='deep')
    sns.set_palette(c1)
    lofm = {}
    to_show = {}
    for i, j in enumerate([-(_*50+300) for _ in range(5)] + [-575]):
        to_show.update(
            {
                (391+i): [("+M_s \\rightarrow %d" % (j),(j - 50)), 'Plusses', +0.5, {}],
            }
        )
    
    j = -625
    to_show[397] = [("-M_s \\rightarrow %d" % (j),(j + 50)), 'Plusses', +0.5, {}]
        
    for nr, content in to_show.items():
        if content[2] == 9.4:
            continue
        options = content[3]
        lofm[nr] = ['$%s \\rightarrow %s\;\mathrm{mT}$' % (
                    content[0][0],
                    content[0][1],
                    ),options]
    
    fig, ax = eva.plot(lofm,
             plot_settings=dict(
                 title='($90^\\circ$) Field Sweeps (Plusses $0.5\;\mathrm{mT}/\mathrm{min}$)',
                 xlim=(1e-2, 1.6e0),
                 ylim=(2e-4, 2e-7)
             ),
             f_settings=dict(
                 xmin=1e-2,
                 ymin=2e-5),
             f2_settings=dict(#disable=True
                 xmin=1e-2,
                 plot_style='k-.',
                 an_color='k',
                 disable=True,
             ),
            )

    with sns.color_palette(c1):
        inset = inset_axes(ax, width='100%', height='90%', 
                           bbox_to_anchor=(.4, .73, .29, .24),
                           bbox_transform=ax.transAxes)
        m.plot_strayfield(inset, 'Strayfield Plusses', nolegend=True)
        inset.legend(['Up ($-M_S \\rightarrow +M_S$)', 'Down ($+M_S \\rightarrow -M_S$)'])
        inset.grid(b=True, alpha=.4)
        inset.set_xlim(-650, 50)
        inset.set_ylim(-.6, .4)
    
        y1, y2 = -1, 2
        for j in [-300-50*i for i in range(5)] + [-575]:
            inset.fill([j, j, j-50, j-50], [y1, y2, y2, y1], alpha=.4)

    plt.savefig('measplan12-2.pdf')

def measplan12_full():
    """Measurement Plan #12 All 14 Measurements in one Graph."""
    #c1 = sns.color_palette("twilight", 14)
    c1 = sns.color_palette("hls", 14)
    ana.set_sns(default=True, grid=True, 
                     size='talk', style='ticks', latex=True)
    sns.set_palette(c1)
    
    
    # Choosing Measurement Numbers to plot
    lofm = {}
    to_show = {
        383: [("+M_s \\rightarrow 25",-25), 'Plusses', +0.5, {}],
        384: [("-25",-75), 'Plusses', +0.5, {'color': 'orange', 'linestyle': '--'}],
    }
    
    for i in range(6):
        to_show.update(
            {
                (385+i): [("+M_s \\rightarrow %d" % (-(i*50+25)),(-(i*50+25) - 50)), 'Plusses', +0.5, {}],
            }
        )

    for i, j in enumerate([-(_*50+300) for _ in range(5)] + [-575]):
        to_show.update(
            {
                (391+i): [("+M_s \\rightarrow %d" % (j),(j - 50)), 'Plusses', +0.5, {}],
            }
        )
    
    j = -625
    to_show[397] = [("-M_s \\rightarrow %d" % (j),(j + 50)), 'Plusses', +0.5, {}]

    # Converting them to a list of measurements (lofm)
    for nr, content in to_show.items():
        if content[2] == 9.4:
            continue
        options = content[3]
        lofm[nr] = ['$%s \\rightarrow %s\;\mathrm{mT}$' % (
                    content[0][0],
                    content[0][1],
                    ),options]
    
    fig, ax = eva.plot(lofm,
             plot_settings=dict(
                 title='($90^\\circ$) Field Sweeps (Plusses;' + \
                         ' $\\Delta B = 50\\mathrm{mT}$;' + \
                         ' $0.5\\;\\mathrm{mT}/\\mathrm{min}$)',
                 xlim=(1e-2, 1.6e0),
                 ylim=(5e-2, 5e-8),
                 legend_settings=dict(loc='best', ncol=2)
             ),
             f_settings=dict(
                 xmin=1e-2,
                 ymin=3e-5),
             f2_settings=dict(#disable=True
                 xmin=2e-2,
                 plot_style='k-.',
                 an_color='k'
             ),
            )

    with sns.color_palette(c1):
        inset = inset_axes(ax, width='100%', height='100%', 
                           bbox_to_anchor=(.07, .06, .34, .26),
                           bbox_transform=ax.transAxes)
        m.plot_strayfield(inset, 
                          'Strayfield Plusses', 
                          show_plusses=False,
                          show_crosses=False,
                          nolegend=True)

        y1, y2 = -1, 2
        for j in [25-50*i for i in range(6)] + \
                    [-300-50*i for i in range(5)] + [-575]:
            inset.fill([j, j, j-50, j-50], [y1, y2, y2, y1], alpha=.8)


        inset.plot(m.up_fitted.B, m.up_fitted.Bx8, 'b-',
                   linewidth=1.5, label='Up')
        inset.plot(m.down_fitted.B, m.down_fitted.Bx8, 'r-', 
                   linewidth=3, label='Down')

        inset.legend(loc='best')
    
        inset.grid(b=True, alpha=.4)
        inset.set_xlim(-650, 50)
        inset.set_ylim(-.6, .4)
        inset.set_xlabel('')
        inset.set_ylabel('')


    ax.annotate('Without Saturation', (1.2e-2, 5e-4), color='orange',
                rotation=-55)
    ax.annotate('With Saturation', (1.01e-2, 4e-4), color='orange', 
                rotation=-35)

    plt.savefig('measplan12-full.pdf')


def calc_dpdt(m):
    """
    Args:
        m:
    """
    pass

if __name__ == '__main__':
    #### H Loops
    # Not needed
    plot_single_hloop(nr=429, xlim=(-300,300))
    #plot_hloops2()
    # Not needed (Single -90deg Hloop)
    #plot_hloops4(m=ana.Hloop(155), filename='hloop-parallel-m90',
    #             figtitle="M154: $-90^\\circ$ Parallel measurement")



    #plot_hloops() # First comparison 0 and 45 deg


    # Compare Hloops of Angles with 180 deg difference
    #plot_hloops_95(to_show=a[95]+a[-85], filename='hloop-compare-95')
    #plot_hloops_95(to_show=a[100]+a[-80], filename='hloop-compare-100',
    #               xlim=(-600, 600), crosses_xlim=(-350, 350))
    #plot_hloops_95(to_show=a[105]+a[-75], filename='hloop-compare-105',
    #               xlim=(-500, 500))
    #plot_hloops_95(to_show=a[110]+a[-70], filename='hloop-compare-110',
    #               xlim=(-350, 350), crosses_xlim=(-500, 500))


    # Compare repeated Measurements
    #plot_hloops3([139,140],
    #             inset_xlim=(-60, 60))
    #plot_hloops3([147,148], filename='hloop-repeat-2', xlim=(-450, 450), 
    #             inset_xlim=(-60, 60), inset_ylim=(-0.1, 1.05))
    #plot_hloops3([143,144], filename='hloop-repeat-3', 
    #             xlim=(-200, 200), ylim=(-.5, 4.2),
    #             inset_xlim=(-70, 70), inset_ylim=(0.1, 3.5))
    # plot_hloops_compare_90([416,417,421,422,423,419], 
    #                        filename='hloop-repeat-414-plusses',
    #                        xlim=(-100,100),
    #                        inset_xlim=(-30,-10), inset_ylim=(.2,.7),
    #                        legend_loc='upper right', nograd=True)
    # plot_hloops_compare_90([416,417,421,422,423,419], 
    #             structure='crosses', filename='hloop-repeat-414-crosses',
    #             xlim=(-100,100),
    #             ylim=(-1.26,-.54),
    #             inset_xlim=(-30,-10), inset_ylim=(-1.1,-.71),
    #             legend_loc='upper right', nograd=True)

    # plot_hloops_compare_90([419,428], 
    #                         filename='hloop-repeat-414-plusses',
    #                         xlim=(-600,600), ylim=(-.35,1.1),
    #                         inset_xlim=(-30,-10), inset_ylim=(.2,.7),
    #                         legend_loc='upper right', nograd=True)
    # plot_hloops_compare_90([419,428], 
    #             structure='crosses', filename='hloop-repeat-414-crosses',
    #             xlim=(-300,300),
    #             ylim=(-2.6,-.54),
    #             inset_xlim=(-50,50), inset_ylim=(-2.5,-.61),
    #             legend_loc='upper right', nograd=True)

# =============================================================================
#     for to_show in [[414,415], 
#                     [416,417,419]]:
#         plot_hloops_compare_90(to_show, 
#                                filename='hloop-repeat-%s-plusses2' % to_show[0],
#                                legend_loc='upper right')
#         plot_hloops_compare_90(to_show, 
#                     structure='crosses', filename='hloop-repeat-%s-crosses2' % to_show[0],
#                     ylim=(-1.26,-.4),
#                     inset_xlim=(-75,75), inset_ylim=(-1.26,-.4))
# 
# =============================================================================
    #plot_hloops_compare_90([417,418], filename='hloop-repeat-417')
    #plot_hloops_compare_90([418,419], filename='hloop-repeat-419')

    # Single Hloop of 90 deg
    #plot_hloops4(ylim=(-1.2, 0.4))

    # Compare plus and minus 90 deg Measurements (with and without mirrorerd)
    #plot_hloops_90()
    #plot_hloops_90(filename='hloop-compare-90-mirrored', mirror=True)
    #plot_hloops_90_nofit(filename='hloop-compare-90-mirrored-nofit')

    # Compare Cubes and Trees
    #plot_cubes_trees()

    #plot_hloop_gradient(limit=50)
    #for i in [139, 140, 147, 148]:
    #    plot_hloop_gradient2(ana.Hloop(i), limit=150,
    #                        filename='hloop-gradient-%s' % i)

    #plot_hloop_temp()


    #### Noise
    # Just for Tests (not needed)
    #negative_sweeps()


    # Static field Noise
    #plot_static_fields()

    # Data that is not much worth
    #multiple_fspans()

    # Fast sweeps large area (>= 1 T)
    #fast_sweeprate()
    #fast_sweeprate(show_numbers=[320, 325, 323, 329, 322, 327, 336],
    #               xlim=(-500, 500),
    #               filename='FastSR-2')
    #fast_sweeprate(show_numbers=[320, 325, 323, 329, 322, 327, 336, 333, 332, 331],
    #               xlim=(-500, 500),
    #               filename='FastSR-3',
    #               pos2=True,
    #               title='($90^\circ$) Field sweeps ($\\Delta B \\geq 200\\;\\mathrm{mT}$)')


    # Plots with fits

    # Sweeping inside hysteresis (plus minus 50/75/etc.)
    #first_sweeps()
    #first_sweeps(add=True)

    # Compare different Voltages
    #compare_voltages()
    
    # Compare different Sweep Rates / Temperatures (inside +- 25 mT)
    #compare_sweeprates()
    #sv_temp_effect()

    
    # Measurement Plan 12 (splitted in half)
    #measplan12()
    #measplan12_2()
    
    #measplan12_full()

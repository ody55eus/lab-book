# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:44:13 2020

@author: JP
"""

# %% Init

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


import ana

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ana-SR830DAQ')



ana.set_sns(default=True, grid=True, 
            size='paper', style='ticks', latex=True)


# %% Define Functions
def get_info(m=431, **kwargs):
    ## Regex Structure
    # Nr,     Struct,         deg,        Type1
    # Type2, Field, Date, Time
    # I1, I2, Lock-In (Connections)
    # Voltage In, Resistors (R11, R12)
    # R13, R21
    # Capacitors (C11, C21)
    # Temp
    """
    Args:
        m:
        **kwargs:
    """
    regex = ".*[Mm]([0-9.]*)_([A-Za-z]*)_([0-9.-]*)deg_([A-Za-z]*)_" \
                            +"([A-Za-z]*)_*B_([0-9.-]*)T_([0-9]*)_([0-9]*)_" \
                            +"I1-([0-9\-]*)_I2-([0-9\-]*)_GBIP.-([0-9\-]*)_" \
                            +"Vin-([0-9.]*)V_R11-([0-9]*.)O_R12-([0-9.]*.)O_" \
                            +"R13-([0-9.]*.)_R21-([0-9.]*.)O_" \
                            +"C11-([0-9]*)_C21-([0-9]*)_" \
                            +"T-([0-9]*)K.*"
    files = glob('data/Data/m%s/*' % m)
    # sns.set_palette(sns.color_palette("hls", len(files)))

    meas = {}
    all_data = pd.DataFrame({'Field':[], 'Time':[], 'Vx':[], 'Vy':[]})
    for f in files:
        reg = re.match(regex, f)
        if not reg:
            logger.error("Regex doesn't match filename: %s" % f)
            continue

        nr, struct, deg, type1, \
            type2, field, date, time, \
            i1, i2, lock_in, \
            vin, r11, r12, r13, r21, \
            c11, c21, Temp = reg.groups()
    
        field = float(field); nr = float(nr)
        
        data_df = pd.read_csv(f, sep='\t')
        if len(data_df['Vx'])%1024:
            d = data_df['Vx'].iloc[:-(len(data_df['Vx'])%1024)]
        else:
            d = data_df.Vx
        
        max_len = len(d)

        data = {'data': d, 
                'info': {
                    'nr': nr,
                    'field': field
                    }
                }
        
        
        # Calculate the first spectrum
        meas[field] = ana.RAW_Measurement(data, 
                                          rate=1/data_df.time.diff().mean(), 
                                          nof_first_spectra=kwargs.get('num_first_spectra', 32),
                                          calc_first=True)
    
        tmp_df = pd.DataFrame({'Field': field,
                           'Time': data_df.time.iloc[:max_len],
                           'Vx': data_df.Vx.iloc[:max_len]*kwargs.get('factor', 1e3),
                           'Vy': data_df.Vy.iloc[:max_len]*kwargs.get('factor', 1e3),
                           })
        all_data = pd.merge(all_data, tmp_df, how='outer')

    return all_data, meas

def plot_info(all_data, meas, show_field=0, **kwargs):
    """
    Args:
        all_data:
        meas:
        show_field:
        **kwargs:
    """
    sns.set_palette(sns.color_palette("hls", len(meas)))
    fig, ((ax11, ax12), \
          (ax21, ax22), \
          (ax31, ax32)) = plt.subplots(nrows=3, ncols=2,
                                       figsize=(11.69,8.27),)
                                       #gridspec_kw=dict(wspace=.3, hspace=.45))
    for field in all_data.sort_values('Field')['Field'].unique():
        # Setting shortcut for Average Spectrum s
        s = meas[field].avg_spec
        ax11.loglog(s.freq, s.S, label='%s T')
        
        # Fitting alpha
        s['lnf'] = np.log10(s.freq)
        s['lnS'] = np.log10(s.S)
        
        if kwargs.get('fit_range'):
            f = scipy.stats.linregress(s.lnf.iloc[:kwargs.get('fit_range')], 
                                       s.lnS.iloc[:kwargs.get('fit_range')])
        else:
            f = scipy.stats.linregress(s.lnf, s.lnS)
        meas[field].info['alpha'] = -f.slope,
        meas[field].info['power'] = f.intercept
    
        ax21.plot(field, -f.slope, 'o')
        ax12.plot(field, 10**f.intercept, 'o')
        ax22.plot(field, s.S.sum(), 'o')
    
        time_df = all_data.query('Field == %f' % field)
        m = time_df['Vx'].mean()
        std = time_df['Vx'].std()
        ax32.errorbar(field, m, yerr=2*std, elinewidth=4, capsize=4)

    xmin, ymin = kwargs.get('xymin', (4e-1, 6e-15))
    factor, alpha = (1.5, 1)
    ax11.plot([xmin,xmin*factor], [ymin, ymin/(factor**alpha)], 'k--')
    ax11.annotate('$1/f$', (xmin*np.sqrt(factor), ymin/(factor**(alpha/2))))

    ax11.set_title('Noise PSD')
    ax11.set_xlabel('$f$ [$\\mathrm{Hz}$]')
    ax11.set_ylabel('$S_V (f)$ [$\\mathrm{V}^2/\\mathrm{Hz}$]')

    ax12.set_title('Noise Fit at 1 Hz')
    ax12.set_ylabel('$S_V (f=1\\,\\mathrm{Hz})$ [$\\mathrm{V}^2/\\mathrm{Hz}$]')

    ax21.set_title('Fit slope')
    ax21.set_ylabel('$\\alpha$')

    ax22.set_title('Noise Sum')

    for ax in [ax22, ax12]:
        ax.set_yscale('log')

    # Show specific field
    try:
        field_data = all_data.query('Field == %f' % show_field)
        field_data.plot(x='Time', y='Vx', legend=False, ax=ax31)
        ax31.set_title('Timesignal ($B_{ext} = %.2f\\,\\mathrm{mT}$)' % (show_field*1e3))
        ax31.set_ylabel('$V_x$ [$%s\\mathrm{V}$]' % (kwargs.get('unit', 'm')))
        
        # show first spectra generated
        len_first_spectra = len(field_data)/kwargs.get('num_first_spectra', 32)
        ymin, ymax = field_data.Vx.min(), field_data.Vx.max()
        for i in range(1, kwargs.get('num_first_spectra', 32)):
            x = field_data.iloc[int(len_first_spectra*i)]['Time']
            ax31.plot([x, x], [ymin, ymax], 'b-', linewidth=.5)

    except Exception as e:
        logger.error("Can not Plot Time signal for field (%s): %s" % (show_field, e))

    ax32.set_title('Hysteresis Loop')
    ax32.set_ylabel('$V_x$ [$%s\\mathrm{V}$]' % (kwargs.get('unit', 'm')))
    ax32.set_xlabel('$\\mu_0 H_{ext}$ [$T$]')

    fig.suptitle('m%s: ' % kwargs.get('nr', 431) \
                 +'Rate=$%s\\,\\mathrm{Hz}$,' % kwargs.get('rate',
                        int(1/all_data.iloc[:500].Time.diff().mean())) \
                 +' Length=$%s\\,\\mathrm{s}$ %s' % (kwargs.get('length', 
                                                    int(time_df.Time.max())),
                                                kwargs.get('add_info', '')))


def plot_various_noise_repr(all_data, meas):
    """
    Args:
        all_data:
        meas:
    """
    sns.set_palette(sns.color_palette("hls", len(meas)))
    fig, axes = plt.subplots(nrows=4, ncols=4,
                                     gridspec_kw=dict(wspace=.3, hspace=.45))
    for i in range(16):
        ax = axes[i//4][i%4]
        for field in all_data.sort_values('Field', ascending=False)['Field'].unique():
            # Setting shortcut for Average Spectrum s
            s = meas[field].avg_spec
    
            ax.plot(field, s.iloc[i]['S'], 'o')
            ax.set_title('$S_V (f=%.3f)$' % s.iloc[i].freq)

def plot_various_noise_fits(all_data, meas, **kwargs):
    """
    Args:
        all_data:
        meas:
        **kwargs:
    """
    sns.set_palette(sns.color_palette("hls", len(meas)))
    fig, axes = plt.subplots(nrows=kwargs.get('nrows',3), 
                             ncols=kwargs.get('ncols',3),
                             gridspec_kw=dict(wspace=.3, hspace=.45),
                             figsize=(11.69, 8.27))
    for i, fit_range in enumerate(kwargs.get('fit_ranges', range(3,11))):
        ax = axes[i//kwargs.get('nrows',3)][i%kwargs.get('ncols',3)]
        for field in all_data.sort_values('Field', ascending=False)['Field'].unique():
            # Setting shortcut for Average Spectrum s
            s = meas[field].avg_spec
            fit = scipy.stats.linregress(s.lnf.iloc[:fit_range], 
                                         s.lnS.iloc[:fit_range])

            if kwargs.get('value', 'intercept') == 'intercept':
                ax.plot(field, 10**fit.intercept, 'o')
                ax.set_yscale('log')
            else:
                ax.plot(field, -1*fit.slope, 'o')

            ax.set_title('Fit Range = %s' % fit_range)
    fig.suptitle(kwargs.get('title', 'Noise Fit at 1 Hz'))


def plot_various_timesignals(all_data, fields, **kwargs):
    """
    Args:
        all_data:
        fields:
        **kwargs:
    """
    fig, axes = plt.subplots(nrows=kwargs.get('nrows',3), 
                             ncols=kwargs.get('ncols',3),
                             figsize=(11.69,8.27))
    for i, f in enumerate(fields):
        ax = axes[i//kwargs.get('nrows',3)][i%kwargs.get('ncols',3)]
        d = all_data[all_data['Field'] == f].iloc[:kwargs.get('plot_range', -1)]
        ax.plot(d['Time'], d['Vx'])
        ax.legend(['$V_x (B_{ext}=%.1f\\,\\mathrm{mT})$' % (f*1e3)])


# %% Def DataFrame and Spectra Dictionary
if not isinstance(df, dict):
    df, spec = {}, {}


# %% Calc Spectra
num = 64
if True:
    for nr in [454 + i for i in range(2)]:
        df[nr], spec[nr] = get_info(m=nr, num_first_spectra=num)


# %% Analyze Data
if True:
    for nr, sf in [
                   # (430, -.01), 
                   # (431, 0), 
                   # (432, 0),
                   # (433, .02),
                   # (434, -.02),
                   # (435, -.026),
                   # (436, .01),
                   # (437, .01),
                   # (438, .01),
                   # (439, .01),
                   # (440, .01),
                   # (441, .01),
                   # (442, .01),
                   # (443, .0),
                   # (444, .0),
                   # (445, .0),
                   # (446, .0),
                   # (447, .0),
                   # (448, 0),
                   # (449, 0),
                   #(450, 0),
                   #(451, 0)
                   # (452,0),
                   # (453,0),
                   # (454,0), (Not working: not enough data points)
                    (455,0.01),
            ]:
        if nr in [430, 431, 440, 441]:
            fit = 10
            xymin = (4e-1, 6e-15)
        else:
            fit = 10
            xymin = (1e-1, 6e-15)
        rate = int(1/df[nr].iloc[:500].Time.diff().mean())
        length = int(df[nr].groupby('Field').max().iloc[5].Time)
        plot_info(df[nr], spec[nr], fit_range=fit, xymin=xymin, nr=nr, 
                  rate=rate, length=length, show_field=sf, 
                  add_info='nofSpectra: %s' % num,
                  num_first_spectra=num)
        plt.savefig('m%s_nofSpectra-%s.png' % (nr, num))

# %% Plot Hysteresis
if False:
    n1 = len(spec[430])
    n2 = len(spec[431])
    sns.set_palette(sns.color_palette("hls", n1+n2))
    fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(16,10))
    for nr in [430, 431]:
        for field in df[nr].sort_values('Field')['Field'].unique():
            s = spec[nr][field].avg_spec
            ax1.plot(field, s.S.sum(), 'o')
            ax2.plot(field, spec[nr][field].info['power'], '*')
    ax1.set_title('Noise Sum')
    ax2.set_title('Noise Power @ 1 Hz')

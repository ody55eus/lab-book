from glob import glob
import ana

from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import seaborn as sns
import pandas as pd
import numpy as np
import scipy.stats


def m456(ax, nr=456):
    files = glob('data/MFN/m%s/*' % nr)
    m456_df = pd.DataFrame({'time':[], 'Vx':[], 'Vy':[]})
    for f in files:
        tmp_df = pd.read_csv(f, sep='\t')
        if not m456_df.empty:
            tmp_df['time'] += m456_df['time'].max()

        m456_df = pd.concat([m456_df, tmp_df])#, how='outer')

    d = m456_df['Vx']
    if len(d)%1024:
        d = d.iloc[:-(len(d)%1024)]

    data = {'data': d, 
            'info': {
                'nr': nr,
                'field': 0,
                }
            }

    m456_spectrum = ana.RAW(data, 
                            rate=1/m456_df['time'].diff().mean(),
                            nof_first_spectra=64,
                            calc_first=True,
                            calc_second=True
                           )
    s = m456_spectrum.avg_spec
    fit_start = 50
    fit_range = 1300
    # Fitting alpha
    s['lnf'] = np.log10(s.freq)
    s['lnS'] = np.log10(s.S)

    f = scipy.stats.linregress(s.lnf.iloc[fit_start:fit_range], 
                               s.lnS.iloc[fit_start:fit_range])

    ax.loglog(s.freq, s.S)
    ax.loglog(s.freq.iloc[fit_start:], 10**(f.intercept)*s.freq.iloc[fit_start:]**f.slope)
    
    return m456_spectrum


def load_data(datapath, focus='Vin', cut=-2):
    meas_data = {}
    meas_info = {}
    all_data = {}
    for f in datapath:
        f_info = ana.measurement.MeasurementClass().get_info_from_name(f)
        sr = f_info[focus]
        nr = f_info['nr']
        meas_info[sr] = f_info
        meas_data[sr] = pd.read_csv(f, sep='\t')
        new_df = meas_data[sr]
        new_df[focus] = float(sr[:cut])
        if nr in all_data.keys():
            all_data[nr] = pd.concat([all_data[nr], new_df])
        else:
            all_data[nr] = new_df
    return meas_data, meas_info, all_data


def calc_PSD(meas_data):
    meas_obj = {}
    for sr, data_df in meas_data.items():
        if len(data_df['Vx']) % 1024:
            avg = len(data_df['Vx']) // 1024
            d = data_df['Vx'].iloc[:-(len(data_df['Vx']) % 1024)]
        else:
            d = data_df.Vx

        max_len = len(d)

        data = {
                    'data': d,
                    'info': {
                        'Nr': 0,
                        'rate': 1 / data_df.time.diff().mean(),
                        'length': max_len * data_df.time.diff().mean(),
                    }
                }

        meas_obj[sr] = ana.RAW(data,
                             rate=data['info']['rate'],
                             nof_first_spectra=32,
                             calc_first = True,
                             downsample=False,
                             )
    return meas_obj

def merge_data(meas_obj, cutoff_frequency=.9, cut=-2):
    diff_voltages = pd.DataFrame()
    for sr, m in meas_obj.items():
        s = m.avg_spec
        s = s[s.freq < cutoff_frequency]
        if len(s) < 2:
            continue
        newdf = pd.DataFrame()
        newdf['freq'] = s.freq
        newdf['S'] = s.S
        newdf['Vin'] = float(sr[:cut])
        diff_voltages = pd.concat([diff_voltages, newdf])
    return diff_voltages


def plot_PSD_classic(diff_voltages, title, groupby_category='SR', group_name='T/min',
                     num=10, style=[['science'], {'context': 'talk', 'style': 'white', 'palette': 'bright',}]):
    c1 = sns.color_palette("hls", num)
    sns.set_palette(c1)
    fig, ax = plt.subplots(figsize=(16,12))
    #g = sns.relplot(x='freq', y='S', hue='Vin', data=diff_voltages, height=5, kind='line')
    grouped  = diff_voltages.groupby(groupby_category)
    for group in grouped.groups.keys():
        if group == 0:
            grouped.get_group(group).plot(x='freq', y='S', kind='line', 
                                          loglog=True, ax=ax, 
                                          label='%.1e %s' % (group, group_name),
                                          color='black',
                                          xlabel='Frequency [Hz]',
                                          ylabel='$S_{V_H}$ [$\\mathrm{V}^2/\\mathrm{Hz}$]',
                                         )
        else:
            grouped.get_group(group).plot(x='freq', y='S', kind='line', 
                                          loglog=True, ax=ax, 
                                          label='%.1e %s' % (group, group_name),
                                          xlabel='Frequency [Hz]',
                                          ylabel='$S_{V_H}$ [$\\mathrm{V}^2/\\mathrm{Hz}$]',
                                         )
    ax.set_title(title)
    #save_plot('m506', 'png')
    
    return ax

def show_PSD_classic(diff_voltages, title, ax=None, groupby_category='Vin', group_name=r'$\mu A$',
                     num=10, style=[['science'], {'context': 'talk', 'style': 'white', 'palette': 'bright',}]):
    if not ax:
        fig, ax = plt.subplots(figsize=(12,8))
    c1 = sns.color_palette("hls", num)
    sns.set_palette(c1)
    #g = sns.relplot(x='freq', y='S', hue='Vin', data=diff_voltages, height=5, kind='line')
    grouped  = diff_voltages.groupby(groupby_category)
    for group in grouped.groups.keys():
        grouped.get_group(group).plot(x='freq', y='S', kind='line', 
                                      loglog=True, ax=ax, 
                                      label='%s %s' % (group*1e-3, group_name),
                                      xlabel='Frequency [Hz]',
                                      ylabel='$S_{V_H}$ [$\\mathrm{V}^2/\\mathrm{Hz}$]',
                                     )
    ax.set_title(title)
    return ax

def plot_PSD_contour(meas_obj, diff_voltages, title,
                     cutoff_frequency=.9,
                     groupby_category='Vin'):
    diff_voltages_contour = pd.DataFrame()
    for sr, m in meas_obj.items():
        s = m.avg_spec
        s = s[s.freq < cutoff_frequency]
        if len(s) < 2:
            continue
        diff_voltages_contour[float(sr[:-2])] = s.S

    v = diff_voltages[groupby_category].unique()
    v.sort()
    frequencies = diff_voltages.freq.unique()
    smin, smax = diff_voltages.S.min(), diff_voltages.S.max()
    levels = np.logspace(np.log10(smin),
                         np.log10(smax), 10)

    fig, ax = plt.subplots(figsize=(12,8))
    cs = ax.contourf(v, frequencies, diff_voltages_contour,
                     norm=LogNorm(vmin=smin, vmax=smax),
                     levels=levels,
                     cmap=plt.cm.Blues,
                     )
    cbar = plt.gcf().colorbar(cs, ax=ax)
    cbar.set_label('$S_V^{V_{in}} (f)$')
    cbar.set_ticklabels(['%.1e' % _ for _ in levels])
    ax.set_yscale('log')
    ax.set_ylabel('$f$ [Hz]')
    ax.set_xlabel('$V_{in}$ [$m$V]')
    ax.set_title(title)


def plot_diff_volt(nr=508, figsize=(16,12)):
    datapath = glob(f'./data/MFN/m{nr}/*')
    meas_data, meas_info, all_data = load_data(datapath)
    meas_obj = calc_PSD(meas_data)
    diff_voltages = merge_data(meas_obj)
    fig, ax = plt.subplots(figsize=figsize)
    show_PSD_classic(diff_voltages, f'm{nr}: Compare different input current amplitudes', ax=ax)

    inset2 = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=(.54, .75, .3, .25),
                       bbox_transform=ax.transAxes)
    inset3 = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=(.1, .1, .3, .25),
                       bbox_transform=ax.transAxes)

    grouped = diff_voltages.groupby('Vin')
    for group in grouped.groups.keys():
        g = grouped.get_group(group)
        fit_area = g.query('freq > %f and freq < %f' % (2e-2, 7e-1))
        fit_area['lnf'] = np.log10(fit_area.freq)
        fit_area['lnS'] = np.log10(fit_area.S)
        fit = scipy.stats.linregress(fit_area.lnf, fit_area.lnS)
        intercept, slope = fit.intercept, -fit.slope
        voltage = group*1e-3

        inset2.plot(voltage, 10**intercept, 'o')
        inset3.plot(voltage, slope, 'o')

    inset2.set_xlabel(r'Current [$\mu\mathrm{A}$]')
    inset2.set_ylabel('$S_{V_H} (f=1\\;$Hz$)$')
    inset2.set_yscale('log')

    inset3.set_xlabel(r'Current [$\mu\mathrm{A}$]')
    inset3.set_ylabel('$\\alpha$')

def plot_diff_sweeprates(nr=507, figsize=(16,12)):
    datapath = glob(f'./data/MFN/m{nr}/*')
    meas_data, meas_info, all_data = load_data(datapath, focus='SR', cut=None)
    meas_obj = calc_PSD(meas_data)
    f_max = (8/(2*np.pi))
    diff_voltages = merge_data(meas_obj, cutoff_frequency=f_max, cut=None)
    title = 'm%s: Different Sweeprates ($\\tau = 100~\\mathrm{ms}$; $f_{Ref} = 17~\\mathrm{Hz}$)' % nr
    ax = plot_PSD_classic(diff_voltages, title, groupby_category='Vin')

    inset2 = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=(.15, .5, .3, .25),
                       bbox_transform=ax.transAxes)
    inset3 = inset_axes(ax, width='100%', height='100%', 
                       bbox_to_anchor=(.08, .09, .3, .24),
                       bbox_transform=ax.transAxes)

    grouped = diff_voltages.groupby('Vin')
    for group in grouped.groups.keys():
        g = grouped.get_group(group)
        fit_area = g.query('freq > %f and freq < %f' % (8e-2, 7e-1))
        fit_area['lnf'] = np.log10(fit_area.freq)
        fit_area['lnS'] = np.log10(fit_area.S)
        fit = scipy.stats.linregress(fit_area.lnf, fit_area.lnS)
        intercept, slope = fit.intercept, -fit.slope
        
        if group == 0:
            continue
        
        voltage = group*1e3

        inset2.plot(voltage, 10**intercept, 'o')
        inset3.plot(voltage, slope, 'o')

    inset2.set_xlabel('Sweeprate [$\\mathrm{mT}/\\mathrm{min}$]')
    inset2.set_ylabel('$S_{V_H} (f=1\\;$Hz$)$')
    inset2.set_yscale('log')

    inset3.set_xlabel('Sweeprate [$\\mathrm{mT}/\\mathrm{min}$]')
    inset3.set_ylabel('$\\alpha$')

import ana
import logging
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(name)s\t[%(levelname)-8s]\t%(message)s')
    logger = logging.getLogger('Compare')
    ana.set_sns(notebook=True, set_mpl_params=True)

    numbers = []
    if len(sys.argv) > 1 and len(sys.argv) % 2:
        for i in range(len(sys.argv[1:])//2):
            numbers.append([int(sys.argv[2*i+1]),
                            int(sys.argv[2*i+2])]
                           )

    # Alternative csv if feather is not available
    mfn_info = pd.read_csv('src/measurement_info.dat')
    #mfn_info = pd.read_feather('measurement_info')
    mfn_info.set_index('index', inplace=True)
    mfn_info.index.name = 'Nr'
    mfn_measurements = {}
    for n in numbers:
        logger.info('Processing Nr. %s' % n)
        fig, axes = plt.subplots(nrows=1, ncols=2, sharey='row',
                                 figsize=(15, 10))
        smin = 1
        smax = 0
        spectra_df = {}
        for j, number in enumerate(n):
            mfn = ana.MFNMeasurement([], nr=number)
            mfn.read("psd_data/m%s" % number)
            fields = mfn.data.sort_values('Field')['Field'].unique()
            spectra_df[number] = pd.DataFrame()
            for f in fields:
                spectra_df[number][f] = mfn.measurements[f].avg_spec.S
            smin = np.min([smin, spectra_df[number].min().min()])
            smax = np.max([smax, spectra_df[number].max().max()])
            mfn_measurements[number] = mfn

        for j, number in enumerate(n):
            ax = axes[j % 2]
            info = mfn_info.loc[number]
            mfn = mfn_measurements[number]
            mfn.spectra_field_contour(ax,
                                      smin=smin, smax=smax, numlevels=20,
                                      title='m%s: %s Sweep' % (number,
                                                               info['Dir']),
                                      cbar=(j % 2))
        info = mfn_info.loc[n[-1]]
        plt.suptitle('$%s^\\circ$: $f_0 = %s\\,\\mathrm{Hz}$; $T = %s\\,'
                     '\\mathrm{K}$' % (info['Angle'],
                                       info['Frequency'],
                                       info['Temp']))
        plt.savefig('img/m%s-%s_compare_PSD.png' % (n[0], n[1]))
        plt.show()

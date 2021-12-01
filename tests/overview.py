import ana
import matplotlib.pyplot as plt
import pandas as pd
import sys
import logging

if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    loglevel = logging.INFO if arg == 'all' else logging.WARNING
    logging.basicConfig(level=loglevel,
                        format='%(name)s\t[%(levelname)-8s] %(message)s')
    logger = logging.getLogger('Overview')

    ana.set_sns(notebook=True, set_mpl_params=True)

    # Alternative csv if feather is not available
    mfn_info = pd.read_csv('src/measurement_info.dat')
    # mfn_info = pd.read_feather('measurement_info')
    mfn_info.set_index('index', inplace=True)
    mfn_info.index.name = 'Nr'

    mfn_measurements = {}
    numbers = mfn_info.query('Error != True and '
                             'Dir != "STATIC" and '
                             'Nr > 480').index.tolist()
    
    for nr in numbers:
        logger.info("Running Nr. %s" % nr)
        tc = mfn_info['timeconstant'].loc[nr] if mfn_info['timeconstant'].loc[nr] else 1

        mfn_measurements[nr] = ana.MFNMeasurement(nr, timeconstant=tc)
        if mfn_measurements[nr].data.empty:
            continue
        
        stat = mfn_measurements[nr].data.groupby('Field').describe()['Vx']
        idxmax = (stat['max'] - stat['min']).idxmax()
        mfn_measurements[nr].plot_info(show_field=idxmax, numlevels=20)
        plt.savefig('img/overview/m%s_cont_info.png' % nr)

        mfn_measurements[nr].write('psd_data/m%s' % nr)

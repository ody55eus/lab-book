Readme
======

.. contents:: Content
    :local:

This python module calculates the fourier transformation of a
``numpy.ndarray`` (or ``pandas.DataFrame``) and computes the power spectral
density of the signal.


Setup
-----


To install the module into the system simply execute setup.py

.. code-block:: console

    $ python setup.py install

Usage
-----

Prepare the signal and important known information about
the signal (like ``rate`` and ``avg``):

.. code-block:: python

   import numpy as np
   signal = np.random.randn(10240) # Normal distributed signal
   rate = 8 # Hz
   avg = len(signal)/1024

Then create an instance of the class ``SpectrumAnalyzer`` which analyzes the
signal (the following are the default settings):

.. code-block:: python

   from spectrumanalyzer import SpectrumAnalyzer
   spectrum = SpectrumAnalyzer(
                    timesignal=signal,
                    samplingrate=rate,
                    averages=avg,
                    shifting_method=False,
                    short_mode=1,
                    filter_type='lowpass',
                    passband_factor=1,
                    filter_order=6,
                    filter_analog=False,
                    first_spectra_highest_frequency=rate/8,
                    downsample=True,
                    )

To calculate the power spectral density, call the function
``cut_timesignal(num)`` and process the returned single spectra as shown: 

.. code-block:: python

   all_spectra = []
   for single_spectrum, \
           frequency_span_array, \ 
           k in spectrum.cut_timesignal(64): # cut into 64 Spectra 
       all_spectra.append(single_spectrum)
   averaged_spectrum = spectrum.first_spectrum_avg


**Optional**: Plot the signal and the PSD:

.. code-block:: python

   import matplotlib.pyplot as plt
   fig, (ax, ax2) = plt.subplots(2)
   ax.plot(np.arange(0, len(signal)/rate, 1/rate), signal)
   ax.set_title('Signal')

   ax2.loglog(frequency_span_array, avgeraged_spectrum)
   ax2.set_title('PSD of Signal')
   plt.show()



Calculation steps for the first spectrum 
----------------------------------------

The following steps are done automatically by ``cut_timesignal(num)``:


#. Cutting the signal into ``num`` parts.

#. Apply a lowpass filter to each signal part.

#. If ``downsample`` is True  
   
   * use every ``gap = (RATE / first_spectra_highest_frequency)`` Point.  

#. Calculate the fourier transformation.  
   
   * [if ``downsample`` and ``shifting_method`` is both True]: Take average of fourier transformed shifted points (shifted by ``gap``).

#. Calculate power spectral density (PSD) by taking squared absolute values.

#. Normalize with normalization factor.

#. Return a single PSD for the ``k``th part of the signal.

#. When ``k == num`` the averaged spectrum is returned.

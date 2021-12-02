Adjustable Parameters
---------------------

Every parameter can have a crucial influence on the measurement. 
Therefore together with each measurement the corresponding used parameters are documented.


Measurement Parameters
~~~~~~~~~~~~~~~~~~~~~~

The following parameters can be adjusted:

.. csv-table::
   :header: Parameter,Description

   T, Temperature of the sample
   |theta|, Angle between sensor and magnetic field
   Type, Measurement Type (Gradio/Hloop/MFN). Determines |I1| and |I2|
   |I1|, Hall bar connection of |I1|
   |I2|, Hall bar connection of |I2|
   Gate, Gate grounding (w/ one bar connection)
   |R1|, see Gradiometry Setup above
   |R2|, see Gradiometry Setup above
   |C1|, see Gradiometry Setup above
   |C2|, see Gradiometry Setup above


Magnet Parameters
~~~~~~~~~~~~~~~~~

.. csv-table::
   :header: Parameter,Description

   |Bext|, External field [T]
   sweep, Sweeping the field?
   SR, Sweeprate of the field [mT/min]
   |dB|, Fieldrange [T]


Lock-In Parameters
~~~~~~~~~~~~~~~~~~

The programmable Lock-In SR830 can be used in various settings:

.. csv-table::
   :header: Parameter,Description
   
   |fref|, Reference Frequency for the signal generator
   |Vin|, Input Voltage
   |tau|, Time Constant (lowpass filter)
   sens, Sensitivity: Highest measurable voltage (-sens < |VH| < +sens)
   Float/Ground, Grounding the signal. Default: Ground
   AC/DC, AC-Coupling. Default: AC
   A/A-B, Input to use. Default: A-B
   Reserve, Noise-Reserve. Default: Normal
   Source, |fref| Source. Default: Internal


Noise Parameters
~~~~~~~~~~~~~~~~

Signal Analyzer (SR785)
+++++++++++++++++++++++

.. csv-table::
   :header: Parameter,Description
   
   |fmax| / Freq-Span, Maximum frequency in the |psd|
   Avg, Number of averages to sample over


Pre Amplifier (SR560)
+++++++++++++++++++++

.. csv-table::
   :header: Parameter,Description

   Gain Mode, Default: Low
   Gain, Default: 200
   Coupling, Default: AC
   Output (50 |ohm|), Default: LI Input A
   Filters, Default: Off

Data Aquisition (DAQ)
+++++++++++++++++++++

.. csv-table::
   :header: Parameter,Description
   
   |rate| / Rate, Sampling Frequency [samples / second]
   Avg, Number of averages to sample over
   |fmax| / Freq-Span, Maximum frequency in the |psd|
   ``downsample``, Sample a part of the signal according to |rate|
   ``shifting_method``, With ``downsample``
   filtering signal, see `SpectrumAnalyzer <../modules/sa/index>`_
   ``zero_padding``, Adding 0 for missing values

.. todo:: implement ``zero_padding`` (currently different length measurements result in data loss. See <http://gitlab.com/ody55eus/ana/-/blob/master/ana/mfn.py#L223>)

.. |psd| replace:: power spectral density
.. |theta| unicode:: U+003B8 .. GREEK SMALL LETTER THETA
.. |mu| unicode:: U+003BC .. GREEK SMALL LETTER MU
.. |tau| unicode:: U+003C4 .. GREEK SMALL LETTER TAU
.. |ohm| unicode:: U+003A9 .. GREEK CAPITAL LETTER OMEGA
.. |R1| replace:: :math:`R_1` 
.. |R2| replace:: :math:`R_2`
.. |C1| replace:: :math:`C_1` 
.. |C2| replace:: :math:`C_2`
.. |I1| replace:: :math:`I_1` 
.. |I2| replace:: :math:`I_2`
.. |Vin| replace:: :math:`V_{in}`
.. |VH| replace:: :math:`V_H`
.. |fref| replace:: :math:`f_{ref}`
.. |fmax| replace:: :math:`f_{max}`
.. |rate| replace:: :math:`f_{sample}`
.. |Bext| replace:: :math:`B_{ext}`
.. |dB| replace:: :math:`dB_{ext}`

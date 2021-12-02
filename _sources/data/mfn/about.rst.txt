===================
About MFN
===================


.. contents:: Content
    :local:

The following section is about the fluctuations of the magnetic system.


.. figure:: ../img/hloops_crosses.png
   :width: 100%
   :target: ../../_static/hloops_crosses.pdf

   Repeated hysteresis loops (Crosses).

.. figure:: ../img/hloops_plusses.png
   :width: 100%
   :target: ../../_static/hloops_plusses.pdf

   Repeated hysteresis loops (Plusses).


Signal Analyzer
---------------

These measurements have been performed with the SR785.


SR785 Signal Analyzer
+++++++++++++++++++++

The signal analyzer SR785 is in-situ calculating the Fourier transformation of a signal.
This yields faster results and improved memory usage because the raw signal does not need to be saved.
This also implies that the raw signal is not available for further analysis.

.. figure:: ../img/sr785-fast.png
   :width: 100%
   :target: ../../_static/sr785-first.pdf

   SR785: Large field sweeps outside and covering the hysteresis.

.. figure:: ../img/sr785-first.png
   :width: 100%
   :target: ../../_static/sr785-first.pdf

   SR785: Field sweeps inside the hysteresis.

Influence of various parameters on the PSD
++++++++++++++++++++++++++++++++++++++++++

Temperature
~~~~~~~~~~~

.. figure:: ../img/sr785-temp.png
   :width: 100%
   :target: ../../_static/sr785-temp.pdf

   SR785: Field sweeps at different temperatures.

Sweeprate
~~~~~~~~~

.. figure:: ../img/sr785-sweeprates.png
   :width: 100%
   :target: ../../_static/sr785-sweeprates.pdf

   SR785: Field sweeps for different sweeprates.

Applied Current Amplitude
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../img/sr785-voltages.png
   :width: 100%
   :target: ../../_static/sr785-voltages.pdf

   SR785: Field sweeps with different applied currents.

SR830 Data Acquisition (SR830DAQ)
---------------------------------

These measurements have been performed solely with the SR830 lock-in amplifier.

Time-Signals
++++++++++++

The SR830 can be programmed to send automatically data to the computer.
Using this feature it is possible to acquire the raw (unfiltered) data.

.. figure:: ../img/hist446_1.png
   :width: 49%
   :target: ../../_static/hist447_2.pdf

   SR830DAQ: Time-Signal’s KDEs at static positions (m446).

.. figure:: ../img/hist447_2.png
   :width: 49%
   :target: ../../_static/hist447_2.pdf

   SR830DAQ: Time-Signal’s KDEs at static positions (m447).

.. figure:: ../img/daq-time-446.png
   :width: 100%
   :target: ../../_static/daq-time-446.pdf

   SR830DAQ: Time-Signal at selected positions (m446).

.. figure:: ../img/daq-time-447.png
   :width: 100%
   :target: ../../_static/daq-time-447.pdf

   SR830DAQ: Time-Signal at selected positions (m447).

.. figure:: ../img/daq-time-446-2.png
   :width: 100%
   :target: ../../_static/daq-time-446-2.pdf

   SR830DAQ: Time-Signal at selected positions (m446).

Analysis Overview
+++++++++++++++++

.. figure:: ../img/daq-info-446.png
   :width: 100%
   :target: ../../_static/daq-info-446.pdf

   SR830DAQ: Analysis Overview (m446).

.. figure:: ../img/daq-info-447.png
   :width: 100%
   :target: ../../_static/daq-info-447.pdf

   SR830DAQ: Analysis Overview (m447).


Calculated PSD
++++++++++++++

.. figure:: ../img/daq-sweeprate.png
   :width: 100%
   :target: ../../_static/daq-sweeprate.pdf

   SR830DAQ: Field sweeps for different sweeprates.


.. figure:: ../img/daq-volt.png
   :width: 100%
   :target: ../../_static/daq-volt.pdf

   SR830DAQ: Field sweeps with different applied currents.

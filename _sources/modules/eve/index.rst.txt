.. _EVE:

Efficient Virtual Environment (EVE)
===================================

.. contents:: Content
    :local:

Basic Structure
---------------

EVE is the main program to perform all measurements and collect all data in the working group of Prof. Jens Müller.
It was programmed in collaboration by this working group’s students over the last years and continuously extended
(see also :ref:`Credits <eve-credits>`).
The graphical user interface (GUI) of EVE is based on the popular PyQt project and supports adding multiple instruments to a measurement process.

.. figure:: img/eve-structure.png

   Functional flowchart diagram of EVE’s fundamental objects

Instruments
-----------

To ensure the safety of the instruments, I scrutinized some algorithms for errors and updated them if necessary.


Lock-In Amplifier
~~~~~~~~~~~~~~~~~

SR830
+++++

The SR830 from Stanford Research is a highly sensitive Lock-In amplifier and a core element of most measurements.
For this project, I programmed a Data Aquisition Mode (DAQ) for fast measurements.
This permits measuring the data at a sampling rate between
:math:`62.5\;\mathrm{mHz} \leq f_S \leq 512\;\mathrm{Hz}`.

There are three different ways to use the DAQ mode:

*FAST*:
The Lock-In sends continuously every ``timestep = 1/rate`` a value to EVE which is stored into a variable. When pressing stop (or after :math:`2^{14}` Points a timeout occurs), EVE converts the data into the Unit V using the sensitivity from the Lock-In at the start of the measurements.

*Single*:
A single measurement is performed, measuring a given number of samples and reading them all in one step (after the time expires) and saving them into the file.

*Loop*:
Multiple Single measurements in a loop until the stop button is pressed. Between each measurement the internal buffer of the lock in is reset to avoid an overflow.


HF2LI
+++++

The High Frequency Lock-In (HF2LI) by Zurich Instruments is a fully digital Lock-In amplifier.


Magnetic Power Supply (IPS120)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The intelligent magnetic power supply (IPS120) controls the superconducting magnet inside the cryostat.
It features the possibility of a persistent magnetic field.
To ensure that nothing breaks in this process, I created a flowchart diagram of the existing algorithm.
The following flowchart pictures the internal programming structure of the two buttons **Goto Set** and **Goto Zero** (which change the magnetic field):

.. figure:: img/IPS120.png

   Flowchart Diagram of IPS120 Magnetic Power Supply Algorithm

Automated Measurements
----------------------

EVE supports scheduled measurements, effectively programming changing variables and running loops to run predefined measurements and automatically change parameters on the fly.
The following figure shows a screenshot of a sample measurement, where the magnet sweeps to various fields and the lock-in measures in-between these sweeps:

.. figure:: img/EVE-scheduled.png

   Scheduled Measurement Example

Saving Routine Files
~~~~~~~~~~~~~~~~~~~~

These measurements can be saved into `routine files <https://gitlab.com/ody55eus/master-data/-/tree/master/measurement_routines>`_ which have the following structure:

.. figure:: img/EVE-routine.png

   EVE Routine File Structure


License
-------

.. warning:: EVE does not have a license yet and can not be published at this point. But it uses licensed software as dependencies and has to comply with these licenses.

.. figure:: img/EVE-packages.svg

   EVE Dependencies and Licensing Compliances

.. _abstract-1:

Abstract
--------

The detailed understanding of micro–and nanoscale structures, in
particular their magnetization dynamics, dominates contemporary
solid–state physics studies. Most investigations already identified an
abundance of phenomena in one–and two–dimensional nanostructures. The
following thesis focuses on the magnetic fingerprint of
three–dimensional :math:`\mathrm{CoFe}` nano–magnets, specifically the
temporal development of their hysteresis loop. These nano–magnets were
grown in a tetrahedral pattern on top of a highly susceptible home–build
:math:`\mathrm{GaAs}/\mathrm{AlGaAs}` micro–Hall sensor using focused
electron beam induced deposition (FEBID).

During the measurements, utmost efforts were employed to exemplify
current best research practices. The data life cycle of the present
thesis is based upon open–source data science tools and packages. Data
acquisition and analysis required self–written automated algorithms to
handle the extensive quantity of data. Existing instrumental–controlling
software was improved, and new Python packages were devised to analyze
and visualize the gathered data. The open–source Python data analysis
framework (``ana``) was developed to facilitate computational
reproducibility. This framework transparently analyses and visualizes
the gathered data automatically using Continuous Analysis tools based on
GitLab and Continuous Integration. This automatization uses bespoke
scripts combined with virtualization tools like Docker to facilitate
reproducible and device–independent results.

The hysteresis loops reveal distinct differences in subsequently
measured loops with identical initial experimental parameters,
originating from the nano–magnet’s magnetic noise. This noise amplifies
in regions where switching processes occur. In such noise–prone regions,
the time–dependent scrutinization reveals presumably thermally induced
metastable magnetization states. The frequency–dependent power spectral
density uncovers a characteristic :math:`1/f^2` behavior at noise–prone
regions with metastable magnetization states.

Summary and Conclusion
----------------------

The present study aims to find and characterize fluctuations in the
magnetic fingerprint of three–dimensional nano–tetrapods. These
tetrapods were deposited by means of focused electron beam induced
deposition (FEBID) on top of a micro–Hall magnetometer. The micro–Hall
measurements scrutinized the magnetic fingerprint by measuring the
nanostructures’ stray–field during an external field sweep and obtaining
the hysteresis loop. Repetitions of identical experiments yield several,
nearly equivalent hysteresis loops that differ in noise–prone regions
near the remanence. These noise–prone regions are further investigated
using statistical methods to determine the noise’s power spectral
density (PSD).

During the process of data acquisition and analysis, utmost efforts were
employed to comply with current best research practices. In general, the
data processing steps involve customized, self–written computer
algorithms that are freely available and fundamentally documented. Based
on experiences, the workflow's documentation process evolved from
proprietary OneNote notebooks towards an open–source driven Continuous
Analysis infrastructure, allowing automated data analysis and
interoperable documentation. In detail, a self–maintained GitLab server
provides the infrastructure to manage git repositories that
version–control data, code, and documentation. In addition, Continuous
Integration tools automate tasks and increase productivity. These
aforementioned data processing and workflow steps have been
fundamentally documented, converted into a presentable format, and made
online available via the supplemental information.

The noise investigations utilized two separate methods to dissect the
Hall signal of the nano–tetrapods during an external field sweep.
Firstly, a signal–analyzer examines the signal’s PSD :math:`S_V (f)` in
the frequency domain. This examination discloses a :math:`1/f^2`
correlation of the PSD only when measuring the stray–field during an
external magnetic field sweep inside a noise–prone region. This
correlation is noteably invariant to changes in the temperature or
sweeprate. A novel data acquisition technique (SR830DAQ) further
scrutinizes this fluctuating nature of the nano–tetrapods’ magnetic
response. This SR830DAQ technique corroborates preceding findings on
:math:`1/f^2` correlations. Additionally, sensitive fluctuations,
although not detectable in a pre–amplified signal with the
signal–analyzer, measured by the SR830DAQ technique, reveal a
:math:`S_V \sim I^2` current dependence of the PSD and confirming
expectations. Closer inspection of the persisting time–signal of
interrupted field sweeps inside the hysteresis loop’s noise–prone
regions exposes metastable magnetization states with spontaneous
switching processes. The author deduces that this spontaneous switching
originates from thermal activation processes.

Key Points
~~~~~~~~~~

-  Best practices were pursued by fundamentally documenting and
   publishing both, data workflow and analysis methods. A self–written
   Python data analysis framework (``ana``) was created for a
   transparent evaluation and Continuous Analysis methods were employed
   to automate time–invasive tasks.
-  The magnetic fingerprint of FEBID deposited three–dimensional
   nano–tetrapods revealed fluctuations with a characteristic
   :math:`1/f^2` behavior. These characteristics were further
   investigated by means of data acquisition methods. The time–signal at
   magnetization states with assumed complex, vortex–like magnetization
   discloses metastable states with spontaneous switching processes.
   These switching processes are concluded to arise from thermally
   activation.

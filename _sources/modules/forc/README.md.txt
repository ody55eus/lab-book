# Analysing FORC Data
This python script converts comma / tab separated value (csv) files from a specific format into a FORCinel readable format.

## Usage
Assuming an Input as multiple csv files (with a space as separator) like the following Table:  
<table><thead><tr><th>$H_{ext}$</th><th>$V_H$</th></tr>
    <tr><th>units</th><th>units</th></tr></thead>
    <tr><td>$H_0$</td><td>$V_0$</td></tr>
    <tr><td>$H_i$</td><td>$V_i$</td></tr>
    <tr><td>$H_N$</td><td>$V_N$</td></tr>
</table>
The unit row is being ignored by this script.
Optional a third row with the temperature is valid (need to change code in the end).
Adjust `folder` to the place where you've put your `*.dat` files.
$`V_i`$ will be devided by `current` to determine the resistance $`R_i`$.

## File structure
The csv input files should use the following naming convention:
* Every File contains `HA=` in the name to determine the reversal Field $H_A$
 * Immediately after `HA=` must be the field value followed by `.dat`
* Down Sweeps: contain the word `down_to` in the name and will be ignored
* Saturation Measurements at $`H_S`$ (containing only information about the saturation field value): contain the word `_sat_`
* All other files are up sweeps from $`H_A`$ to $`H_S`$

### Example
```
Some_Ignored_Informations_down_to_HA=1.500000.dat
Some_Ignored_Informations_sat_HA=1.500000.dat
Some_Ignored_Informations_upinformation_HA=1.500000.dat
Some_Ignored_Informations_down_to_HA=0.000000.dat
Some_Ignored_Informations_sat_HA=0.000000.dat
Some_Ignored_Informations_upinformation_HA=0.000000.dat
Some_Ignored_Informations_down_to_HA=-1.500000.dat
Some_Ignored_Informations_sat_HA=-1.500000.dat
Some_Ignored_Informations_upinformation_HA=-1.500000.dat
```

## Output
The output will be a file `output.dat` which contains a header that is readable by FORCinel and a Table like the following:
<table width=200px>
    <tr><td>$\langle H_S\rangle$</td><td>$\langle R_S \rangle$</td></tr>
    <tr><td>$H_{A_1}$</td><td>$R(H_{A_1})$</td></tr>
    <tr><td>$H_S$</td><td>$R(H_S)$</td></tr>
    <tr><td></td><td></td></tr>
    <tr><td>$\langle H_S\rangle$</td><td>$\langle R_S \rangle$</td></tr>
    <tr><td>$H_{A_2}$</td><td>$R(H_{A_2})$</td></tr>
    <tr><td>$H_{i}$</td><td>$R(H_i)$</td></tr>
    <tr><td>$H_S$</td><td>$R(H_S)$</td></tr>
</table>
With 2 entries for the first reversal field $H_{A_1}$ and one more entry with each following reversal field (ordered by the magnitude of the reversal fields starting at $\max(H_{A_i})$ and ending at $\min(H_{A_i})$)

### Example
```
MicroMag 2900/3900 Data File (Series 0015)
First-order reversal curves
Configuration   :  VSM
Hardware version:  0004
Software version:  11/20/2006
Units of measure:  mks
Temperature in  :  Kelvin
01/11/2007  15:01
bg1.11 frag c.03 taped sample forc

Averaging time = +1.000000E-01
Hb1            = -1.000000E+03
Hb2            = +1.000000E+03
Hc1            =  0.000000E+00
Hc2            = +3.000000E+03
HCal           = +1.500000E-01
HNcr           = +2.000005E-03
HSat           = +1.500000E-01
NCrv           = 100
PauseCal       = +1.000000E+00
PauseNtl       = +1.000000E+00
PauseSat       = +1.000000E+00
SlewRate       = +1.000000E+04
Smoothing      = 5

Field range    = +1.500000E-01
Moment range   = +1.000000E-02
Temperature    = +0.000000E+00
Orientation    = +9.000001E+01
Elapsed time   = +6.436355E+06
Slope corr.    = N/A
Saturation     = N/A
NData          = 5250

1.500000E+02,1.320206E+00

+4.820400E+01,+1.226155E+00
+1.500000E+02,+1.320205E+00

1.500000E+02,1.320204E+00

+4.620800E+01,+1.221773E+00
+9.810400E+01,+1.293156E+00
+1.500000E+02,+1.320204E+00

1.500000E+02,1.320207E+00

+4.421200E+01,+1.217202E+00
+7.947467E+01,+1.275475E+00
+1.147373E+02,+1.304538E+00
+1.500000E+02,+1.320206E+00
```
## This document is going to calculation the size of the vertical and horizontal tail sizes relative to the wing size. The code is specifically for the design 1 aircraft (without the canards).

# importining pint ($ pip install pint)
import pint
import numpy as np
import matplotlib.pyplot as plt

# using function ureg to convert between metric and imperial
ureg = pint.UnitRegistry()


# Our Calculated/Given variables
S_ref_meter=0.44608787 * ureg.meter**2
S_ref_inch=S_ref_meter.to(ureg.inch**2)

chord_inch=9.6 * ureg.inch
chord_meter=chord_inch.to(ureg.meter)

wingspan_inch=77 * ureg.inch 
wingspan_meter=wingspan_inch.to(ureg.meter)


# Horizontal Tail Sizing Calculations
# C_HT = S_HT * L_HT / ( chord * S_ref)

# C_HT value shoudl be between 0.3-0.6
C_HT=0.3  # unitless

# Educated guess on what L_HT would be
L_HT=18 * ureg.inch

S_HT=C_HT*chord_inch*S_ref_inch/L_HT
print('Surface area of the Horizontal Tail is =', S_HT)

# Estimated Horizontal Tail chord and length
HT_chord=np.array([1,2,3,4,5,6,7,8,9]) * ureg.inch
#print('Chord of Horizontal Tail =', HT_chord)

HT_length=S_HT/HT_chord
#print('Length of Horizontal Tail =', HT_length)

plt.plot(HT_chord,HT_length)
plt.savefig('HT_Sizing.png')
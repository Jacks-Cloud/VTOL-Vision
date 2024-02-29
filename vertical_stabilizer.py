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

chord_inch=9.25 * ureg.inch
chord_meter=chord_inch.to(ureg.meter)

wingspan_inch=62 * ureg.inch 
wingspan_meter=wingspan_inch.to(ureg.meter)



# Vertical Tail Sizing Calculations
# C_VT = S_VT * L_VT / ( wingspan * S_ref)

# C_VT value shoudl be between 0.02-0.05
C_VT=0.02  # unitless

# Educated guess on what L_VT would be
L_VT=11 * ureg.inch

S_VT=C_VT*wingspan_inch*S_ref_inch/L_VT
print('Surface area of the Vertical Tail is =', S_VT)

# Estimated Vertical Tail chord and length
VT_chord=np.array([1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9]) * ureg.inch
#print('Chord of Vertical Tail =', HT_chord)

VT_length=S_VT/VT_chord
#print('Length of Vertical Tail =', HT_length)



plt.plot(VT_chord,VT_length)

plt.title("Vertical Stabilizer Size")
plt.xlabel("Chord Length (inches)")
plt.ylabel("Wingspan Length (inches)")
plt.grid()

plt.savefig('Vertical_Stabilizer_Sizing.png')

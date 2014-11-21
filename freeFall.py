#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10000)
PE = 9.8 * x
KE = 98 - 9.8 * x

plt.plot(x, PE, "b", label = "Potential")
plt.plot(x, KE, "r", label = "Kinetic")
plt.legend(loc = "upper right")

plt.xlabel("Distance Fallen, $\Delta h$ (m)")
plt.ylabel("Energy, $PE$ & $KE$, (J)")


plt.show()
#!/usr/bin/env python

import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10000)

plt.subplot(2, 1, 1)
PE = 9.8 * x
KE = 98 - 9.8 * x

plt.plot(x, PE, "b", label = "Potential")
plt.plot(x, KE, "r", label = "Kinetic")
plt.legend(loc = "upper right")

plt.xlabel("Distance Fallen, $\Delta h$ (m)")
plt.ylabel("Energy, $PE$ & $KE$, (J)")


plt.subplot(2, 1, 2)
t = np.sqrt(2 * x / 9.8)
PE = 9.8 * x
KE = 98 - 9.8 * x

plt.plot(t, PE, "b", label = "Potential")
plt.plot(t, KE, "r", label = "Kinetic")
plt.legend(loc = "upper right")

plt.xlabel("Time Change, $\Delta t$ (s)")
plt.ylabel("Energy, $PE$ & $KE$, (J)")


plt.subplots_adjust(hspace = 0.37)

plt.suptitle("Potential Energy & Kinetic Energy During Free Fall", fontsize = 15)


plt.show()
plt.savefig("KE & PE during free fall.png")
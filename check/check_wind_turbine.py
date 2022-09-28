#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Paul Aubin
# Created Date: 2022/09/27
# ---------------------------------------------------------------------------
""" check Wind Turbine class """
# ---------------------------------------------------------------------------
from wind_turbine import Wind_turbine, Wind
import matplotlib.pyplot as plt
import numpy as np

wt = Wind_turbine()
print(wt)
pw = wt.step(10, 0, 1)
print(pw)
print(wt.heading)
pw = wt.step(10, 0, 0)
print(pw)
print(wt.heading)
pw = wt.step(10, 0, 2)
print(pw)
print(wt.heading)

wind = np.linspace(0, 25, 51)
power_output = []
for w in wind:
	power_output.append(wt.step(w, 0, 1))

plt.plot(wind, power_output)
plt.grid()
plt.show()

wind_heading = np.linspace(0, 360, int(1e3))
power_output = []
for wh in wind_heading:
	power_output.append(wt.step(10, wh, 1))
plt.plot(wind_heading, power_output)
plt.grid()
plt.show()

steps = 360 * [0]
power_output = []
for s in steps:
	power_output.append(wt.step(10, 0, s))
plt.plot(power_output)
plt.grid()
plt.show()
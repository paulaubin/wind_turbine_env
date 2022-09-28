#!/usr/bin/env pythnon3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Paul Aubin
# Created Date: 2022/09/28
# ---------------------------------------------------------------------------
""" Demo to run an agent on the wind turbine environment """
# ---------------------------------------------------------------------------
from wind_turbine import Wind_turbine, Wind
from simu import Basic_agent, Simu
import matplotlib.pyplot as plt

# Set up a wind with 10m/s speed, at 270° from the North, 1s time step,
# at 8AM in the morning and with the Ornstein-Uhlenbeck model
wd = Wind(10, 270, 1, 8*3600, 'OU')

# Set up a wind turbine at 350° of heading angle with inertia enabled
wt = Wind_turbine(350, True)

# Set up an agent that will give the policy
ba = Basic_agent()

# Set up a simulation that lasts 1 day
sm = Simu(ba, wd, wt, 24*3600)

# Run the simulation
sm.run_simu()

# Get the log from the simulation
power_output = sm.power_output_log
actions = sm.action_log
rel_wind = sm.rel_wind_heading_log

# Plot the result
ax1 = plt.subplot(311)
ax1.plot(power_output)
ax1.grid()
ax1.set_ylabel('Power output (MW)')

ax2 = plt.subplot(312, sharex=ax1)
ax2.plot(rel_wind)
ax2.grid()
ax2.set_xlabel('Steps')
ax2.set_ylabel('Relative wind (°)')
ax2.set_ylim((-50, 50))

ax3 = plt.subplot(313, sharex=ax1)
ax3.plot(actions)
ax3.grid()
ax3.set_xlabel('Steps')
ax3.set_ylabel('Action taken')

# Resize
fig = plt.gcf()
fig.set_size_inches(14, 8)

plt.show()
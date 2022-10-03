#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Paul Aubin
# Created Date: 2022/09/27
# ---------------------------------------------------------------------------
""" check wind class """
# ---------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from wind_turbine import Wind


w1_step_size = 1
w2_step_size = 60
duration = 24*3600

w1 = Wind(10, 270, w1_step_size,  'OU')
w2 = Wind(10, 270, w2_step_size, 'OU')

time1 = np.linspace(0, duration, duration+1)
w1_sp_log = np.zeros((np.size(time1), 1))
w1_h_log = np.zeros((np.size(time1), 1))
for t in range(len(time1)) :
	w1_sp_log[t] = w1.speed
	w1_h_log[t] = w1.heading
	w1.step()

time2 = np.linspace(0, duration, int(duration/w2_step_size)+1)
w2_sp_log = np.zeros((np.size(time2), 1))
w2_h_log = np.zeros((np.size(time2), 1))
for t in range(len(time2)) :
	w2_sp_log[t] = w2.speed
	w2_h_log[t] = w2.heading
	w2.step()

print('mean speed 1= ', np.mean(w1_sp_log))
print('std speed 1= ', np.std(w1_sp_log))
print('mean heading 1= ', np.mean(w1_h_log))
print('std heading 1= ', np.std(w1_h_log))

print('mean speed 2= ', np.mean(w2_sp_log))
print('std speed 2= ', np.std(w2_sp_log))
print('mean heading 2= ', np.mean(w2_h_log))
print('std heading 2= ', np.std(w2_h_log))

fig, axs = plt.subplots(2, sharex=True)
axs[0].plot(time1, w1_sp_log, label='step = 1')
axs[0].plot(time2, w2_sp_log, label='step = 10')
axs[0].set(xlabel = 'Time (s)', ylabel='Speed (m/s)')
axs[0].grid()
axs[1].plot(time1, w1_h_log, label='step = 1')
axs[1].plot(time2, w2_h_log, label='step = 10')
axs[1].set(xlabel = 'Time (s)', ylabel='Heading (°)')
axs[1].grid()
fig.set_size_inches(14, 8)
plt.show()
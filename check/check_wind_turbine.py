#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Paul Aubin
# Created Date: 2022/09/27
# ---------------------------------------------------------------------------
""" check Wind Turbine class """
# ---------------------------------------------------------------------------
from wind_turbine import Wind_turbine, Wind

wt = Wind_turbine()
print(wt)
pw = wt.step(10, 0, 1)
print(pw)
pw = wt.step(10, 0, 0)
print(pw)
pw = wt.step(10, 0, 2)
print(pw)
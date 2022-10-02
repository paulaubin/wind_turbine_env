#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Paul Aubin
# Created Date: 2022/09/26
# ---------------------------------------------------------------------------
""" Useful tools """
# ---------------------------------------------------------------------------

import numpy as np

def wrap_to_m180_p180(angle_in_degree : float) -> float :
	"""
	Wrap an angle in degree to [-180, 180]
	"""
	return np.mod(angle_in_degree + 180, 360) - 180

# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:34:21 2015

@author: t.tomski
"""

import time
import numpy as np

start_time = time.time()
for i in range(100000000):
    x = i * i
print("Program execution time (standard):\n--- %s seconds --- " % (time.time() - start_time))
print
start_time = time.time()
x = np.arange(100000000, dtype=np.uint64)
x = np.multiply(x, x)
print("Program execution time (optimized with numpy):\n--- %s seconds --- " % (time.time() - start_time))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Algorithms and Complexity                                 February 23, 2022
IST 4310
Prof. M Diaz-Maldonado

Synopsis:
Shows matplotlib's pyplot can be used for plotting the (x, y) coordinates.

Copyright (c) 2022 Misael Diaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

References:
[0] JJ McConnell, Analysis of Algorithms, 2nd edition, 2007
[1] R Johansson, Numerical Python: Scientific Computing and Data
    Science Applications with NumPy, SciPy, and Matplotlib, 2nd edition
"""

import numpy as np
from matplotlib import pyplot as plt

def read_document(name):
  data = open("{}.txt".format(name), mode="r").read().split("\n")
  sizes = []
  values = []
  
  for line in data:
    if line != "":
      n, time = line.split(" ")
      sizes.append(int(n))
      values.append(float(time))

  return np.array(sorted(sizes)), np.array(sorted(values))

# defines the particle positions as a list of (x, y) coordinates
iterativeSizes, iterativeTimes = read_document("dataIterativo")
recursiveSizes, recursiveTimes = read_document("dataRecursivo")

# closes all figures and enables interactive plotting
plt.close('all')
plt.ion()

# creates a figure and a set of axes
fig, (ax1, ax2) = plt.subplots(2)

fig.suptitle('Iterative (Up) vs recursive (Down) algorithm')

# plots the coordinates as symbols (no lines connecting them)
ax1.plot(iterativeSizes, iterativeTimes, marker='.', markersize=12, color='green')
# sets the axes labels
ax1.set_ylabel('Average execution time')

ax2.plot(recursiveSizes, recursiveTimes, marker='.', markersize=12, color='orange')
# sets the axes labels
ax2.set_xlabel('Number of coords')
ax2.set_ylabel('Average execution time')
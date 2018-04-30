'''
  File name: rmVerSeam.py
  Author:
  Date created:
'''

'''

'''

import numpy as np
# import matplotlib.pyplot as plt
from PIL import Image
from cumMinEngVer import cumMinEngVer

def rmVerSeam(I, Mx, Tbx):
  # print I.shape
  height, width, color = I.shape
  Ix = np.zeros((height, width-1, color))

  E = np.amin(Mx[height-1])
  min_pos = np.argmin(Mx[height-1])
  # print min_last
  # print min_pos
  direct = 0
  for i in range(height):
    Ix[height-i-1][0:min_pos] = I[height-i-1][0:min_pos]
    Ix[height-i-1][min_pos:width-1] = I[height-i-1][min_pos+1:width]
    direct = int(Tbx[height-i-1][min_pos])
    # print direct
    min_pos = min_pos + direct
    # print Ix
  # print Ix
  return Ix, E

# test = np.array([[5.5, 8, 4.5, 6, 3], [13, 9, 30, 27, 19], [6.5, 7, 6, 12.5, 8], [16, 24, 27, 11, 13], [3, 6, 4.5, 8, 5.5]])
# data1 = np.array([[[1, 2, 3], [1, 2, 3], [1, 6, 3], [1, 2, 3], [1, 2, 3]], [[4, 5, 6], [5, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]], [[1, 2, 3], [1, 2, 3], [1, 2, 4], [1, 2, 3], [1, 2, 3]], [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 7, 6], [4, 5, 6]], [[7, 8, 9], [7, 8, 9], [10, 11, 12], [3, 5, 0], [2, 1, 6]]])
# # print data1
# Mx, Tbx = cumMinEngVer(test)

# rmVerSeam(data1, Mx, Tbx)
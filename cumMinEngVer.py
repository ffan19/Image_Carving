'''
  File name: cumMinEngVer.py
  Author:
  Date created:
'''

'''
  File clarification:
'''

import numpy as np
# import matplotlib.pyplot as plt
from PIL import Image

def cumMinEngVer(e):
  height, width = e.shape
  Mx = np.zeros((height, width))
  Tbx = np.zeros((height, width))
  Mx[0] = e[0]

  for i in range(1, height):
    for j in range(width):
      if j == 0:
        Mx[i][j] = e[i][j] + min(Mx[i-1][j], Mx[i-1][j+1])
        if Mx[i-1][j] < Mx[i-1][j+1]:
          Tbx[i][j] = 0
        else:
          Tbx[i][j] = 1
      elif j == (width - 1):
        Mx[i][j] = e[i][j] + min(Mx[i-1][j], Mx[i-1][j-1])
        if Mx[i-1][j] < Mx[i-1][j-1]:
          Tbx[i][j] = 0
        else:
          Tbx[i][j] = -1
      else:
        Mx[i][j] = e[i][j] + min(Mx[i-1][j], Mx[i-1][j+1], Mx[i-1][j-1])
        if Mx[i-1][j] < Mx[i-1][j+1]:
          if Mx[i-1][j] < Mx[i-1][j-1]:
            Tbx[i][j] = 0
          elif Mx[i-1][j-1] < Mx[i-1][j+1]:
            Tbx[i][j] = -1
          else:
            Tbx[i][j] = 1
        elif Mx[i-1][j+1] < Mx[i-1][j-1]:
          Tbx[i][j] = 1
        else:
          Tbx[i][j] = -1

  # print Mx
  # print Tbx
  return Mx, Tbx

# test = np.array([[5.5, 8, 4.5, 6, 3], [13, 9, 30, 27, 19], [6.5, 7, 6, 12.5, 8], [16, 24, 27, 11, 13], [3, 6, 4.5, 8, 5.5]])
# cumMinEngVer(test)
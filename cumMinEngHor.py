'''
  File name: cumMinEngHor.py
  Author:
  Date created:
'''

'''
'''

import numpy as np
# import matplotlib.pyplot as plt
from PIL import Image
from cumMinEngVer import cumMinEngVer

def cumMinEngHor(e):
  my, tby = cumMinEngVer(np.transpose(e))
  My = np.transpose(my)
  Tby = np.transpose(tby)
  # print My
  # print Tby
  return My, Tby

# test = np.array([[5.5, 8, 4.5, 6, 3], [13, 9, 30, 27, 19], [6.5, 7, 6, 12.5, 8], [16, 24, 27, 11, 13], [3, 6, 4.5, 8, 5.5]])

# cumMinEngHor(test)
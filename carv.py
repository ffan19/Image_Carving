'''
  File name: carv.py
  Author:
  Date created:
'''

'''
'''

import numpy as np
# import matplotlib.pyplot as plt
from PIL import Image
from cumMinEngHor import cumMinEngHor
from cumMinEngVer import cumMinEngVer
from rmVerSeam import rmVerSeam
from rmHorSeam import rmHorSeam
from genEngMap import genEngMap
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import signal
import imageio

def carv(I, nr, nc):
  res_list = []
  print I.shape
  height, width, color = I.shape
  T = np.zeros((nr+1, nc+1))
  e = genEngMap(I)
  Ic = I
  Mx, Tbx = cumMinEngVer(e)
  My, Tby = cumMinEngHor(e)
  removed_c = 0
  removed_r = 0
  T[0][1] = np.amin(Mx[height-1])
  My_transpose = np.transpose(My)
  T[1][0] = np.amin(My_transpose[height-1])
  for i in range(nr + nc):
    # print i
    if removed_c == nc:
      print "all columns removed"
      My, Tby = cumMinEngHor(e)
      Ic, E = rmHorSeam(Ic, My, Tby)
      res_list.append(Ic)
      e = genEngMap(Ic)
      removed_r += 1
    elif removed_r == nr:
      print "all rows removed"
      Mx, Tbx = cumMinEngVer(e)
      Ic, E = rmVerSeam(Ic, My, Tby)
      res_list.append(Ic)
      e = genEngMap(Ic)
      removed_c += 1
    elif T[removed_r][removed_c+1] > T[removed_r+1][removed_c]: #here is the problem
      print "romoving row"
      My, Tby = cumMinEngHor(e)
      Ic, E = rmHorSeam(Ic, My, Tby)
      res_list.append(Ic)
      e = genEngMap(Ic)
      removed_r += 1
      Mx, Tbx = cumMinEngVer(e)
      My, Tby = cumMinEngHor(e)
      T[removed_r][removed_c+1] = np.amin(Mx[height-1-removed_r])
      My_transpose = np.transpose(My)
      if (removed_r < nr):
        T[removed_r+1][removed_c] = np.amin(My_transpose[width-1-removed_c])
    else:
      print "removing column"
      Mx, Tbx = cumMinEngVer(e)
      Ic, E = rmVerSeam(Ic, Mx, Tbx)
      res_list.append(Ic)
      e = genEngMap(Ic)
      removed_c += 1
      Mx, Tbx = cumMinEngVer(e)
      My, Tby = cumMinEngHor(e)
      if (removed_c < nc):
        T[removed_r][removed_c+1] = np.amin(Mx[height-1-removed_r])
      My_transpose = np.transpose(My)
      T[removed_r+1][removed_c] = np.amin(My_transpose[width-1-removed_c])
  # print Ic.shape
  imageio.mimsave('./Shanghai2Output.gif', res_list)
  return Ic, T

# test = np.array([[5.5, 8, 4.5, 6, 3], [13, 9, 30, 27, 19], [6.5, 7, 6, 12.5, 8], [16, 24, 27, 11, 13], [3, 6, 4.5, 8, 5.5]])
# data1 = np.array([[[1, 2, 3], [1, 2, 3], [1, 6, 3], [1, 2, 3], [1, 2, 3]], [[4, 5, 6], [5, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]], [[1, 2, 3], [1, 2, 3], [1, 2, 4], [1, 2, 3], [1, 2, 3]], [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 7, 6], [4, 5, 6]], [[7, 8, 9], [7, 8, 9], [10, 11, 12], [3, 5, 0], [2, 1, 6]]])
# carv(data1, 2, 2)

# img1 =  Image.open("shanghai2.jpg")
# data1 = np.asarray(img1, dtype="int32")
# Ic, T = carv(data1, 50, 30)
# Ic = np.asarray(Ic, dtype="uint8")
# plt.imshow(Ic)
# plt.show()
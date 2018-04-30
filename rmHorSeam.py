'''
  File name: rmHorSeam.py
  Author:
  Date created:
'''

'''
'''
import numpy as np
# import matplotlib.pyplot as plt
from PIL import Image
from cumMinEngHor import cumMinEngHor

from rmVerSeam import rmVerSeam

def rmHorSeam(I, My, Tby):
  Ix, Ex = rmVerSeam(np.transpose(I, axes=(1, 0, 2)), np.transpose(My), np.transpose(Tby))
  Iy = np.transpose(Ix, axes=(1, 0, 2))
  E = np.transpose(Ex)
  # print Iy.shape
  # print E
  return Iy, E

test = np.array([[5.5, 8, 4.5, 6, 3], [13, 9, 30, 27, 19], [6.5, 7, 6, 12.5, 8], [16, 24, 27, 11, 13], [3, 6, 4.5, 8, 5.5]])
data1 = np.array([[[1, 2, 3], [1, 2, 3], [1, 6, 3], [1, 2, 3], [1, 2, 3]], [[4, 5, 6], [5, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]], [[1, 2, 3], [1, 2, 3], [1, 2, 4], [1, 2, 3], [1, 2, 3]], [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 7, 6], [4, 5, 6]], [[7, 8, 9], [7, 8, 9], [10, 11, 12], [3, 5, 0], [2, 1, 6]]])
# print data1.shape
My, Tby = cumMinEngHor(test)
# img1 =  Image.open("Test1.jpg")
# data1 = np.asarray(img1, dtype="int32")
rmHorSeam(data1, My, Tby)
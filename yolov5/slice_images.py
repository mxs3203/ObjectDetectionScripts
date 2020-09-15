import PIL
import cv2
import numpy as np
from matplotlib import pyplot as plt

from scipy import ndimage
from scipy import misc
import scipy.misc
import scipy
import image_slicer
from image_slicer import join
from PIL import Image
PIL.Image.MAX_IMAGE_PIXELS = 933120000
img = "E:/Neutrophils_793/1826_19_neutrophils.png"
num_tiles = 2700
tiles = image_slicer.slice(img, num_tiles)


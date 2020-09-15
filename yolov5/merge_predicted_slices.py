import sys

import PIL
import image_slicer
from PIL import Image
import time
PIL.Image.MAX_IMAGE_PIXELS = 933120000
start_time = time.time()
tiles = image_slicer.open_images_in("E:\yolov5\inference\output")
image = image_slicer.join(tiles)
image.save('E:/yolov5/inference/output_conf_08.png')
print("--- %s seconds ---" % (time.time() - start_time))
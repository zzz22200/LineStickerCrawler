import imageio
import os
from apng import APNG
import numpy as np


def apng2gif(imgFile):
    os.system('apng2gif.exe '+imgFile)

    os.remove(imgFile)





import imageio
import os
from apng import APNG
import numpy as np


def apng2gif(imgFile):
    im = APNG.open(imgFile)
    pngframes = []
    for img in enumerate(im.frames):
        pngframes.append(img[1][0])


    frames=np.array(pngframes)
    print(type(frames))
    imageio.mimsave(imgFile[:-4]+'.gif',frames)

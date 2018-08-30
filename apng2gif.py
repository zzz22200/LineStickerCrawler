import imageio
import os
from apng import APNG
import numpy as np


def apng2gif(imgFile,count,fileLocation):
    im = APNG.open(imgFile)
    pngframes = []
    im2 = imageio.imread(imgFile)

    for i, (png, control) in enumerate(im.frames):
        frameFile=fileLocation+"\\{count}-{i}.png".format(i=i,count=count)
        png.save(frameFile)
        im = imageio.imread(frameFile)
        pngframes.append(im)
        os.remove(frameFile)

    os.remove(imgFile)
    imageio.mimsave(imgFile[:-4]+'.gif',pngframes, duration = 0.05)




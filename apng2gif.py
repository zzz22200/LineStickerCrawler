
import os


def apng2gif(imgFile):

    os.system('apng2gif.exe '+imgFile)
    os.remove(imgFile)






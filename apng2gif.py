import os


def apng2gif(imgFile):
    os.system('apng2gif.exe ' + imgFile)
    os.remove(imgFile)
    loopFile=imgFile[:-4]+'.gif'
    os.system('gifsicle  --loopcount=forever '+loopFile+' -o'+loopFile)
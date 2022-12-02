import glob
import subprocess
import random
import os

def randomImage():
    lastLine = subprocess.check_output(['tail', '-1', "logs.txt"])

    images = glob.glob('/home/styx/.backgrounds/Images/*')
    image = random.choice(images)
    
    if lastLine == image:
        randomImage()

    subprocess.Popen(['feh', '--bg-fill', image])

    file = open("logs.txt", "a")
    file.write(image + '\n')
    file.close()

randomImage()

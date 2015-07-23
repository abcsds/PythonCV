from SimpleCV import *
import os
cam = Camera()

while True:
    img = cam.getImage()
    eyes = img.findHaarFeatures(os.getcwd()+"/cascades/eye.xml")
    try:
        for eye in eyes:
            eye.draw((0,255,0))
    except:
        pass
    img.show()

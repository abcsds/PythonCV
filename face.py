from SimpleCV import *
import os
cam = Camera()

while True:
    img = cam.getImage()
    faces = img.findHaarFeatures(os.getcwd()+"/cascades/face.xml")
    try:
        for face in faces:
            face.draw((0,255,0))
    except:
        pass
    img.show()

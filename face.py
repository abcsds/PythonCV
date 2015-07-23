from SimpleCV import *
import os
cam = Camera()

while True:
    img = cam.getImage()
    faces = img.findHaarFeatures(os.getcwd()+"/cascades/face.xml")
    for face in faces:
        face.draw((0,255,0))
    img.show()
    img.save("FaceDetected.jpg")

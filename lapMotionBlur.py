from SimpleCV import *
from operator import add

cam = Camera()
frames_to_blur = 10
frames = ImageSet()

while True:
    frames.append(cam.getImage().edges(t1=160))
    if len(frames) > frames_to_blur:
        frames.pop(0)
    pic = reduce(add, [i / float(len(frames)) for i in frames])
    pic.show()

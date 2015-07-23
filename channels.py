from SimpleCV import *
cam = Camera()
while True:
    img = cam.getImage()
    (red, green, blue) = img.channels()
    # red.show()
    # green.show()
    blue.show()

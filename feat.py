from SimpleCV import *
cam = Camera()
while True:
    img = cam.getImage()
    lines = img.findLines()
    corners = img.findCorners()
    lines.draw(Color.RED)
    corners.draw(Color.BLUE)
    img.show()

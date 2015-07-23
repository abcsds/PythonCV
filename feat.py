from SimpleCV import *

cam = Camera()

while True:
    img = cam.getImage()
    feats = img.findKeypoints()
    feats.draw(color=Color.RED)
    img.show()
    # apply the stuff we found to the image.
    output = img.applyLayers()
    output.show()

from SimpleCV import *
# Make a function that does a half and half image.
def halfsies(left,right):
    result = left
    # crop the right image to be just the right side.
    crop   = right.crop(right.width/2.0,0,right.width/2.0,right.height)
    # now paste the crop on the left image.
    result = result.blit(crop,(left.width/2,0))
    # return the results.
    return result
cam = Camera()
while True:
    # Get Image from camera
    img = cam.getImage()
    # create an edge image using the Canny edge detector
    # set the first threshold to 160
    output = img.edges(t1=160)
    # generate the side by side image.
    result = halfsies(img,output)
    # show the results.
    # result.show()
    output.show()

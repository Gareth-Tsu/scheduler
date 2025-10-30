#Asn3.py: Image processing

import image

def draw_lines(img):
    '''Write code below to draw a green vertical line from top to bottom,
       1/3 of the way across a copy of edinburgh-castle.gif; also draw a
       horizontal blue line 1/3 of the way down the same image. Return
       the copy'''
    copy = img.clone()  #Make a copy of img
    #Draw your green and blue lines on copy
    return copy

def border(img):
    '''Write code below to draw a black border 10 pixels wide around
       the copy; this amounts to drawing 10 black lines across the
       top and bottom and 10 vertical black lines on the left and
       right sides.'''
    copy = img.clone()  #Make a copy of img
    #Draw the borders on copy
    return copy

def blue_roses(img):
    '''Write code below to change the color of the red roses in
       the copy to blue. A good test to find the red rose pixels
       is red > 150 and red > (green + blue) * 1.25.
    '''
    copy = img.clone()  #Make a copy of img
    #Create a blue pixel
    #For each pixel in copy, if the pixel is red replace it with blue
    return copy

def blend(img1, img2):
    '''Write code below to blend .6 of img1 with .4 of img2; assume
       img1 and img2 are the same size'''
    new_image = image.EmptyImage(img1.getWidth(), img1.getHeight())
    #for y in range of the height of new_img
    #    for x in range of the width of new_image
    #        get a pixel from the x, y position of img1
    #        get a pixel from the x, y position of img2
    #        set r to 0.6 * red from img1 pixel + 0.4 * red from img2 pixel
    #        create g & b using the same method as for r
    #        make a new pixel using r, g, and b
    #        set the pixel in the x, y position in new_img to the new pixel
    return new_image

def rotate(img):
    '''OPTIONAL: Write code below to return a copy of img that is
       rotated 90 degrees; you'll have to create an empty image -
       think about what the width and height of that image should
       be. Then copy the pixels from img to the empty image so
       the new image is rotated 90 degrees from img.
    '''
    ...  #Replace this with your code

#Don't change anythign below this point
#(except change .gif to .jpg if you use jpeg images)
def main():
    img1 = image.Image('images//edinburgh-castle.gif')
    new_img1 = draw_lines(img1)
    win1 = image.ImageWin(new_img1.getWidth(), new_img1.getHeight(), "Win1")
    new_img1.draw(win1)
    img2 = image.Image('images//arch.gif')
    new_img2 = border(img2)
    win2 = image.ImageWin(new_img2.getWidth(), new_img2.getHeight(), "Win2")
    new_img2.draw(win2)
    img3 = image.Image('images//beach.gif')
    img4 = image.Image('images//blueMotorcycle.gif')
    img5 = blend(img3, img4)
    win3 = image.ImageWin(img5.getWidth(), img5.getHeight(), "Win3")
    img5.draw(win3)
    img6 = image.Image("images//arch.gif")
    img7 = rotate(img6)
    if img7:
        win7 = image.ImageWin(img7.getWidth(), img7.getHeight(), "Win7")
        img7.draw(win7)
    
main()

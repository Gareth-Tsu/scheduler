# Asn3.py: Image processing

import image

def draw_lines(img):
    '''Write code below to draw a green vertical line from top to bottom,
       1/3 of the way across a copy of edinburgh-castle.gif; also draw a
       horizontal blue line 1/3 of the way down the same image. Return
       the copy'''
    copy = img.clone()  # Make a copy of img
    w, h = copy.getWidth(), copy.getHeight()

    x_line = w // 3
    y_line = h // 3

    green = image.Pixel(0, 255, 0)
    blue = image.Pixel(0, 0, 255)

    # vertical green line at 1/3 width
    for y in range(h):
        copy.setPixel(x_line, y, green)

    # horizontal blue line at 1/3 height
    for x in range(w):
        copy.setPixel(x, y_line, blue)

    return copy

def border(img):
    '''Write code below to draw a black border 10 pixels wide around
       the copy; this amounts to drawing 10 black lines across the
       top and bottom and 10 vertical black lines on the left and
       right sides.'''
    copy = img.clone()  # Make a copy of img
    w, h = copy.getWidth(), copy.getHeight()
    black = image.Pixel(0, 0, 0)
    thickness = 10

    # Top and bottom borders
    for dy in range(thickness):
        y_top = dy
        y_bot = h - 1 - dy
        for x in range(w):
            copy.setPixel(x, y_top, black)
            copy.setPixel(x, y_bot, black)

    # Left and right borders
    for dx in range(thickness):
        x_left = dx
        x_right = w - 1 - dx
        for y in range(h):
            copy.setPixel(x_left, y, black)
            copy.setPixel(x_right, y, black)

    return copy

def blue_roses(img):
    '''Write code below to change the color of the red roses in
       the copy to blue. A good test to find the red rose pixels
       is red > 150 and red > (green + blue) * 1.25.
    '''
    copy = img.clone()  # Make a copy of img
    w, h = copy.getWidth(), copy.getHeight()
    blue_px = image.Pixel(0, 0, 255)

    for y in range(h):
        for x in range(w):
            p = copy.getPixel(x, y)
            r, g, b = p.getRed(), p.getGreen(), p.getBlue()
            if (r > 150) and (r > (g + b) * 1.25):
                copy.setPixel(x, y, blue_px)

    return copy

def blend(img1, img2):
    '''Write code below to blend .6 of img1 with .4 of img2; assume
       img1 and img2 are the same size'''
    w, h = img1.getWidth(), img1.getHeight()
    new_image = image.EmptyImage(w, h)

    for y in range(h):
        for x in range(w):
            p1 = img1.getPixel(x, y)
            p2 = img2.getPixel(x, y)

            r = int(0.6 * p1.getRed()   + 0.4 * p2.getRed())
            g = int(0.6 * p1.getGreen() + 0.4 * p2.getGreen())
            b = int(0.6 * p1.getBlue()  + 0.4 * p2.getBlue())

            new_image.setPixel(x, y, image.Pixel(r, g, b))

    return new_image

def rotate(img):
    '''OPTIONAL: Return a copy of img rotated 90 degrees clockwise.'''
    w, h = img.getWidth(), img.getHeight()
    rotated = image.EmptyImage(h, w)  # note: width=original height, height=original width

    # (x, y) -> (h - 1 - y, x) for clockwise rotation
    for y in range(h):
        for x in range(w):
            p = img.getPixel(x, y)
            rx = h - 1 - y
            ry = x
            rotated.setPixel(rx, ry, p)

    return rotated

# Don't change anything below this point
# (except change .gif to .jpg if you use jpeg images)
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

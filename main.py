from PIL import Image
from numpy import array

path = input("Please provide the path to the image to convert: ")
white_pixel = input("Please enter character to represent white pixel: ")
black_pixel = input("Please enter character to represent black pixel: ")

# open image
img = Image.open(path)

# scale image if too large - this has to fit into a console
if sum(img.size) > 200:
    img.thumbnail((100, 100), Image.ANTIALIAS) # limit img size
arr = array(img)

# convert to black/white
for i, row in enumerate(arr):
    for j, pixel in enumerate(row):
        # 382 is (255+255+255)//2 rounded down to nearest int
        if sum(pixel) > 382:
            print(white_pixel, end="")
        else:
            print(black_pixel, end="")
    print()
    
input() # keeps console open
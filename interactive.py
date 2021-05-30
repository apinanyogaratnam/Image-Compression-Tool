from PIL import Image
from filters import *

filename = "apishan.jpg"
image = Image.open(filename)


# greyscale_filter(image)
green_filter(image)

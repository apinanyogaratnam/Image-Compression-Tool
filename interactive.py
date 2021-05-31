from PIL import Image, ImageFilter
# from utilities import *
from filters import *

filename = "apishan.jpg"
filename = "sky.jpg"
image = Image.open(filename)
image = image.convert('RGB')


luminosity(image, 80)

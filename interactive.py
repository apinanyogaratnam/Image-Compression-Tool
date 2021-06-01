from PIL import Image, ImageFilter
# from utilities import *
from filters import *

filename = "apishan.jpg"
image = Image.open(filename)
image = image.convert('RGB')

blur_filter(image)
from PIL import Image
from filters import *

filename = "apishan.jpg"
image = Image.open(filename)
image = image.convert('RGB')

blur_filter(image)


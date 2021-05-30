from PIL import Image
from filters import *

filename = "sky.png"
image = Image.open(filename)
image = image.convert('RGB')


# greyscale_filter(image)
# green_filter(image)



from PIL import Image
from filters import *

filename = "sky.png"
apishan = "apishan.jpg"
image = Image.open(filename)
image = image.convert('RGB')

greyscale_filter(image)
green_filter(image)
greyscale_alternative_filter(image)
blue_filter(image)
pink_filter(image)
yellow_filter(image)
reduce_opacity_filter(image, 3)


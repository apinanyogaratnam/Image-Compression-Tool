from PIL import Image, ImageFilter
# from utilities import *
from filters import *

filename = "apishan.jpg"
image = Image.open(filename)
image = image.convert('RGB')

origin = (130, 150)
end = (400, 320)

crop(image, origin, end)

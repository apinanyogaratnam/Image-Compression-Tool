from PIL import Image
# from utilities import *
from filters import *

filename = "apishan.jpg"
image = Image.open(filename)
image = image.convert('RGB')


n_dimension = 3


blur_modular_filter(image, n_dimension)



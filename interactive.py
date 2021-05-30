from PIL import Image

filename = "apishan.jpg"

image = Image.open(filename)
# image.show()
pix_val = list(image.getdata())
print(pix_val)
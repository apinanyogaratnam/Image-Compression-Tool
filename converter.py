from PIL import Image

def jpg_to_png(image, filename):
    filename = filename.strip(".jpg")
    image.save(filename + ".png")
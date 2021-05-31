from utilities import *


def greyscale_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        colour_sum = round(current_tuple[0]*0.3) + round(current_tuple[1]*0.59) + round(current_tuple[1]*0.11)
        current_tuple[0] = colour_sum
        current_tuple[1] = colour_sum
        current_tuple[2]= colour_sum
        data.append(tuple(current_tuple))
    
    footer(image, data, "greyscale_filter")


def green_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] = round(current_tuple[0]*0.3)
        current_tuple[1] = round(current_tuple[1]*0.59)
        current_tuple[2]= round(current_tuple[1]*0.11)
        data.append(tuple(current_tuple))
    
    footer(image, data, "green_filter")


def greyscale_alternative_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        avg = round(sum(current_tuple) / 3)
        current_tuple[0] = avg
        current_tuple[1] = avg
        current_tuple[2]= avg
        data.append(tuple(current_tuple))
    
    footer(image, data, "greyscale_alternate_filter")

def blue_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] = 0
        data.append(tuple(current_tuple))
    
    footer(image, data, "blue_filter")


def dark_blue_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[1] = 0
        data.append(tuple(current_tuple))
    
    footer(image, data, "pink_filter")


def yellow_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[2] = 0
        data.append(tuple(current_tuple))

    footer(image, data, "yellow_filter")


def reduce_opacity_filter(image, opacity_level):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] = round(current_tuple[0] / opacity_level)
        current_tuple[1] = round(current_tuple[1] / opacity_level)
        current_tuple[2] = round(current_tuple[2] / opacity_level)
        data.append(tuple(current_tuple))

    footer(image, data, "reduce_opacity_filter")


def blur_filter(image):
    grid = convert_list_to_2d_list(image, image.getdata())

    
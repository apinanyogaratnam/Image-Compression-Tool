from utilities import *
from PIL import Image, ImageFilter, ImageDraw
from math import sqrt

# Constants

# Box Blur kernel
BOX_KERNEL = [[1 / 9, 1 / 9, 1 / 9],
            [1 / 9, 1 / 9, 1 / 9],
            [1 / 9, 1 / 9, 1 / 9]]

# Gaussian kernel
GAUSSIAN_KERNEL = [[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
                [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
                [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]

# High-pass kernel
SHARPEN_KERNEL = [[  0  , -.5 ,    0 ],
        [-.5 ,   3  , -.5 ],
        [  0  , -.5 ,    0 ]]

# Low-pass kernel
UNSHARPEN_KERNEL = [[1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9]]

# Sobel kernels
KERNELX = [[-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]]
KERNELY = [[-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]]


# filter functions
def greyscale_filter(image):
    """
    """

    data = []
    image_data = get_image_data(image)

    # applying greyscale formula for rbg pixels
    for i in range(len(image_data)):
        current_tuple = get_image_data(image)
        colour_sum = round(current_tuple[0]*0.3) + round(current_tuple[1]*0.59) + round(current_tuple[1]*0.11)
        current_tuple[0] = colour_sum
        current_tuple[1] = colour_sum
        current_tuple[2]= colour_sum
        data.append(tuple(current_tuple))
    
    # saving the image
    footer(image, data, "greyscale_filter")


def green_filter(image):
    """
    """
    
    data = []
    image_data = get_image_data(image)

    # applying greyscale formula for rbg pixels differently
    for i in range(len(image_data)):
        current_tuple = get_image_data(image)
        current_tuple[0] = round(current_tuple[0]*0.3)
        current_tuple[1] = round(current_tuple[1]*0.59)
        current_tuple[2]= round(current_tuple[1]*0.11)
        data.append(tuple(current_tuple))
    
    # saving the image
    footer(image, data, "green_filter")


def greyscale_alternative_filter(image):
    """
    """
    
    data = []
    image_data = get_image_data(image)

    # averaging pixel and creating new average pixel
    for i in range(len(image_data)):
        current_tuple = get_image_data(image)
        avg = round(sum(current_tuple) / 3)
        current_tuple[0] = avg
        current_tuple[1] = avg
        current_tuple[2]= avg
        data.append(tuple(current_tuple))
    
    # saving the image
    footer(image, data, "greyscale_alternate_filter")


def blue_filter(image):
    """
    """
    
    data = []
    image_data = get_image_data(image)

    # setting every 'r' pixel to 0
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] = 0
        data.append(tuple(current_tuple))
    
    # saving the image
    footer(image, data, "blue_filter")


def dark_blue_filter(image):
    """
    """
    
    data = []
    image_data = get_image_data(image)

    # setting every 'g' pixel to 0
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[1] = 0
        data.append(tuple(current_tuple))
    
    # saving the image
    footer(image, data, "pink_filter")


def yellow_filter(image):
    """
    """
    
    data = []
    image_data = get_image_data(image)

    # setting every 'b' pixel to 0
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[2] = 0
        data.append(tuple(current_tuple))

    # saving the image
    footer(image, data, "yellow_filter")


def reduce_opacity_filter(image, opacity_level):
    """
    """
    
    data = []
    image_data = get_image_data(image)

    # creating new opacity level pixels
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] = round(current_tuple[0] / opacity_level)
        current_tuple[1] = round(current_tuple[1] / opacity_level)
        current_tuple[2] = round(current_tuple[2] / opacity_level)
        data.append(tuple(current_tuple))

    # saving the image
    footer(image, data, "reduce_opacity_filter")


def blur_filter_3x3(image):
    """
    """
    
    # gathering image data
    size_of_image = image.size
    width = size_of_image[0]
    image_data = get_image_data(image)

    data = []

    # averaging pixels and creating new averaged pixels
    for i in range(len(image_data)):
        p1, p2, p3 = i, i+1, i+2
        p4, p5, p6 = p1 + width, p1 + width + 1, p1 + width + 2
        p7, p8, p9 = p4 + width, p4 + width + 1, p4 + width + 2

        if (p9 > len(image_data)-1): break

        average_tuple = get_average_tuple([image_data[p1], image_data[p2], image_data[p3], image_data[p4], image_data[p5], image_data[p6], image_data[p7], image_data[p8], image_data[p9]])
        data.append(average_tuple)
    
    # saving the image
    footer(image, data, "blur_filter3x3")


def blur_filter_4x3(image):
    """
    """

    # gathering image data
    size_of_image = image.size
    width = size_of_image[0]
    image_data = get_image_data(image)

    data = []

    # averaging pixels and creating new averaged pixels
    for i in range(len(image_data)):
        p1, p2, p3, p4 = i, i+1, i+2, i+3
        p5, p6, p7, p8 = p1 + width, p1 + width + 1, p1 + width + 2, p1 + width + 3
        p9, p10, p11, p12 = p5 + width, p5 + width + 1, p5 + width + 2, p5 + width + 3

        if (p12 > len(image_data)-1): break

        average_tuple = get_average_tuple([image_data[p1], image_data[p2], image_data[p3], image_data[p4], image_data[p5], image_data[p6], image_data[p7], image_data[p8], image_data[p9], image_data[p10], image_data[p11], image_data[p12]])
        data.append(average_tuple)
    
    # saving the image
    footer(image, data, "blur_filter4x3")


def blur_lib_filter(image, level_of_blur):
    """Blur an image depending on level_of_blur from 0 to 100
    """

    # blur the image using pillow lib
    image = image.filter(ImageFilter.GaussianBlur(level_of_blur))

    # saving the image
    footer_without_data(image, "blurry_image_filter")


def luminosity_filter(image, level_of_luminosity):
    """Filter increases or reduces luminosity depeneding on
    level_of_luminosity
    """

    data = []
    image_data = get_image_data(image)

    # add level of luminosity to every rgb pixel
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] += level_of_luminosity
        current_tuple[1] += level_of_luminosity
        current_tuple[2] += level_of_luminosity
        data.append(tuple(current_tuple))
    
    # saving the image
    footer(image, data, "luminosity_filter")


def contrast_filter(image):
    """
    """
    
    contrast_min = 0
    contrast_max = 0

    data = []
    image_data = get_image_data(image)

    # get image min and max contrast
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        avg = (current_tuple[0] + current_tuple[1] + current_tuple[2]) / 3
        contrast_min = min(avg, contrast_min)
        contrast_max = max(avg, contrast_max)
    
    # apply formula of contrast using min and max contrast
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        avg = (current_tuple[0] + current_tuple[1] + current_tuple[2]) / 3

        if (avg == 0): continue

        # new luminosity
        new = 255 * (avg - contrast_min) / (contrast_max - contrast_min)

        current_tuple[0] = int(current_tuple[0] * new / avg)
        current_tuple[1] = int(current_tuple[1] * new / avg)
        current_tuple[2] = int(current_tuple[2] * new / avg)
    
    # saving the image
    footer(image, data, "luminosity_filter")


def crop_filter(image, upper_left_coordinates, bottom_right_coordinates):
    """
    """
    
    # Load image
    pixels = image.load()

    # Cropped coordinates
    origin = upper_left_coordinates
    end = bottom_right_coordinates

    # Create a new cropped image
    output_image = Image.new("RGB", (end[0] - origin[0], end[1] - origin[1]))
    draw = ImageDraw.Draw(output_image)

    # Copy pixels
    for x in range(output_image.width):
        for y in range(output_image.height):
            x_pixel, y_pixel = x + origin[0], y + origin[1]
            draw.point((x, y), pixels[x_pixel, y_pixel])

    # saving the image
    footer_without_data(output_image, "cropped_image")


def blur_filter(image):
    """
    """
    
    # Load image:
    pixels = image.load()

    # Select kernel here:
    kernel = GAUSSIAN_KERNEL

    # Middle of the kernel
    offset = len(kernel) // 2

    # Create output image
    output_image = Image.new("RGB", image.size)
    draw = ImageDraw.Draw(output_image)

    # Compute convolution between intensity and kernels
    for x in range(offset, image.width - offset):
        for y in range(offset, image.height - offset):
            acc = [0, 0, 0]
            for i in range(len(kernel)):
                for j in range(len(kernel)):
                    xn = x + i - offset
                    yn = y + j - offset
                    pixel = pixels[xn, yn]
                    acc[0] += pixel[0] * kernel[i][j]
                    acc[1] += pixel[1] * kernel[i][j]
                    acc[2] += pixel[2] * kernel[i][j]

            draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))

    # saving the image   
    footer_without_data(output_image, "blur_filter")


def sharpen_filter(image):
    """
    """
    
    # Load image:
    pixels = image.load()

    # select kernel
    kernel = SHARPEN_KERNEL

    # Middle of the kernel
    offset = len(kernel) // 2

    # Create output image
    output_image = Image.new("RGB", image.size)
    draw = ImageDraw.Draw(output_image)

    # Compute convolution with kernel
    for x in range(offset, image.width - offset):
        for y in range(offset, image.height - offset):
            acc = [0, 0, 0]
            for i in range(len(kernel)):
                for j in range(len(kernel)):
                    xn = x + i - offset
                    yn = y + j - offset
                    pixel = pixels[xn, yn]
                    acc[0] += pixel[0] * kernel[i][j]
                    acc[1] += pixel[1] * kernel[i][j]
                    acc[2] += pixel[2] * kernel[i][j]

            draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
      
    # saving the image
    footer_without_data(output_image, "sharpen_filter")


def unsharpen_mask_filter(image, amount):
    """
    """
    
    # Load image:
    pixels = image.load()

    # select kernel
    kernel = UNSHARPEN_KERNEL

    # Middle of the kernel
    offset = len(kernel) // 2

    # Create output image
    output_image = Image.new("RGB", image.size)
    draw = ImageDraw.Draw(output_image)

    # Compute convolution with kernel
    for x in range(offset, image.width - offset):
        for y in range(offset, image.height - offset):
            original_pixel = pixels[x, y]
            acc = [0, 0, 0]
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = pixels[xn, yn]
                    acc[0] += pixel[0] * kernel[a][b]
                    acc[1] += pixel[1] * kernel[a][b]
                    acc[2] += pixel[2] * kernel[a][b]

            new_pixel = (
                int(original_pixel[0] + (original_pixel[0] - acc[0]) * amount),
                int(original_pixel[1] + (original_pixel[1] - acc[1]) * amount),
                int(original_pixel[2] + (original_pixel[2] - acc[2]) * amount)
            )
            draw.point((x, y), new_pixel)
    
    # saving the image
    footer_without_data(output_image, "unsharpen_mask_filter")


def edge_detection_filter(image):
    """
    """
    
    # Load image:
    pixels = image.load()

    # Calculate pixel intensity as the average of red, green and blue colors.
    intensity = [[sum(pixels[x, y]) / 3 for y in range(image.height)] for x in range(image.width)]

    # Create output image
    output_image = Image.new("RGB", image.size)
    draw = ImageDraw.Draw(output_image)

    # Compute convolution between intensity and kernels
    for x in range(1, image.width - 1):
        for y in range(1, image.height - 1):
            magx, magy = 0, 0
            for i in range(3):
                for j in range(3):
                    xn = x + i - 1
                    yn = y + j - 1
                    magx += intensity[xn][yn] * KERNELX[i][j]
                    magy += intensity[xn][yn] * KERNELY[i][j]

            # Draw in black and white the magnitude
            color = int(sqrt(magx**2 + magy**2))
            draw.point((x, y), (color, color, color))
    
    # saving the image
    footer_without_data(output_image, "edge_detection_filter")

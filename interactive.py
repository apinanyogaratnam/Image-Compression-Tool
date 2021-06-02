from PIL import Image, ImageFilter
from utilities import *
from filters import *


def print_options():
    print("1. Greyscale filter")
    print("2. Green filter")
    print("3. Alternate greyscale filter")
    print("4. Blue filter")
    print("5. Dark blue filter")
    print("6. Yellow filter")
    print("7. Reduce opacity filter")
    print("8. Slight blur 3x3 filter")
    print("9. Slight blur 4x3 filter")
    print("10. Blur filter")
    print("11. Luminosity filter")
    print("12. Contrast filter")
    print("13. Crop image filter")
    print("14. Slight blur filter")
    print("15. Sharpen filter")
    print("16. Unsharpen mask filter")
    print("17. Edge detection filter")
    print("18. Exit program")


repeat = True
while (repeat):
    repeat_opening_image = True
    while(repeat_opening_image):
        try:
            image_name = input("Enter the image file name with the extension: ")
            image = Image.open(image_name)
            image = image.convert('RGB')
            repeat_opening_image = False
        except:
            print("File unable to open.")
            repeat_opening_image = True

    print_options()
    selection = int(input("Enter a number to select an option: "))
    
    if (selection == 1):
        greyscale_filter(image)
        repeat = False
    elif (selection == 2):
        green_filter(image)
        repeat = False
    elif (selection == 3):
        greyscale_alternative_filter(image)
        repeat = False
    elif (selection == 4):
        blue_filter(image)
        repeat = False
    elif (selection == 5):
        dark_blue_filter(image)
        repeat = False
    elif (selection == 6):
        yellow_filter(image)
        repeat = False
    elif (selection == 7):
        level_of_opacity = input("Level of opacity: ")
        reduce_opacity_filter(image, level_of_opacity)
        repeat = False
    elif (selection == 8):
        blur_filter_3x3(image)
        repeat = False
    elif (selection == 9):
        blur_filter_4x3(image)
        repeat = False
    elif (selection == 10):
        level_of_blur = input("Enter level of blur from 1-100: ")
        blur_lib_filter(image, level_of_blur)
        repeat = False
    elif (selection == 11):
        level_of_luminosity = input("Level of luminosity: ")
        luminosity_filter(image, level_of_luminosity)
        repeat = False
    elif (selection == 12):
        contrast_filter(image)
        repeat = False
    elif (selection == 13):
        x = input("Enter upper x-coordinate: ")
        y = input("Enter upper y-coordinate: ")
        upper_left_coordinates = (x, y)
        x = input("Enter lower x-coordinate: ")
        y = input("Enter lower y-coordinate: ")
        bottom_right_coordinates = (x, y)
        crop_filter(image, upper_left_coordinates, bottom_right_coordinates)
        repeat = False
    elif (selection == 14):
        blur_filter(image)
        repeat = False
    elif (selection == 15):
        sharpen_filter(image)
        repeat = False
    elif (selection == 16):
        unsharpen_mask_filter(image)
        repeat = False
    elif (selection == 17):
        edge_detection_filter(image)
        repeat = False
    elif (selection == 18):
        repeat = False
        exit()
    else:
        print("Invalid option.")
        repeat = True


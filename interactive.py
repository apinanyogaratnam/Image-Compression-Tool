from PIL import Image, ImageFilter
from utilities import *
from filters import *


# different options for user to select
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


# error checking for correct selected input
repeat = True
while (repeat):
    # error checking for correct file opened
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

    # error checking for correct option selection
    repeat_selection = True
    while (repeat_selection):
        try:
            selection = int(input("Enter a number to select an option: "))
            repeat_selection = False
        except:
            print("Invalid input.")
            repeat_selection = True
    
    # filter selection options
    if (selection == 1):
        print("Loading...", end="\r")
        greyscale_filter(image)
        repeat = False
    elif (selection == 2):
        print("Loading...", end="\r")
        green_filter(image)
        repeat = False
    elif (selection == 3):
        print("Loading...", end="\r")
        greyscale_alternative_filter(image)
        repeat = False
    elif (selection == 4):
        print("Loading...", end="\r")
        blue_filter(image)
        repeat = False
    elif (selection == 5):
        print("Loading...", end="\r")
        dark_blue_filter(image)
        repeat = False
    elif (selection == 6):
        print("Loading...", end="\r")
        yellow_filter(image)
        repeat = False
    elif (selection == 7):
        print("Loading...", end="\r")
        level_of_opacity = input("Level of opacity: ")
        reduce_opacity_filter(image, level_of_opacity)
        repeat = False
    elif (selection == 8):
        print("Loading...", end="\r")
        blur_filter_3x3(image)
        repeat = False
    elif (selection == 9):
        print("Loading...", end="\r")
        blur_filter_4x3(image)
        repeat = False
    elif (selection == 10):
        level_of_blur = input("Enter level of blur from 1-100: ")
        print("Loading...", end="\r")
        blur_lib_filter(image, level_of_blur)
        repeat = False
    elif (selection == 11):
        level_of_luminosity = input("Level of luminosity: ")
        print("Loading...", end="\r")
        luminosity_filter(image, level_of_luminosity)
        repeat = False
    elif (selection == 12):
        print("Loading...", end="\r")
        contrast_filter(image)
        repeat = False
    elif (selection == 13):
        x = input("Enter upper x-coordinate: ")
        y = input("Enter upper y-coordinate: ")
        upper_left_coordinates = (x, y)
        x = input("Enter lower x-coordinate: ")
        y = input("Enter lower y-coordinate: ")
        bottom_right_coordinates = (x, y)
        print("Loading...", end="\r")
        crop_filter(image, upper_left_coordinates, bottom_right_coordinates)
        repeat = False
    elif (selection == 14):
        print("Loading...", end="\r")
        blur_filter(image)
        repeat = False
    elif (selection == 15):
        print("Loading...", end="\r")
        sharpen_filter(image)
        repeat = False
    elif (selection == 16):
        amount = input("Enter amount of unsharpenness from 1-10: ")
        print("Loading...", end="\r")
        unsharpen_mask_filter(image, amount)
        repeat = False
    elif (selection == 17):
        print("Loading...", end="\r")
        edge_detection_filter(image)
        repeat = False
    elif (selection == 18):
        repeat = False
        exit()
    else:
        print("Invalid option.")
        repeat = True

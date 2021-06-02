def footer_without_data(image, name_of_file):
    """Saves an image with the given name_of_file and saves it as 
    user's desired file extension
    """

    # file_extension = get_validated_file_extension()
    file_extension = ".jpg"
    image.save("./expected_filter_results/" + name_of_file + file_extension)
    print("Image saved in " + name_of_file + file_extension)
    image.show()


def footer(image, data, name_of_file):
    """Saves an image with the given name_of_file and saves it as 
    the user's desired file extension using data as the data as the newly 
    formed pixels
    """

    image.putdata(data)
    # file_extension = get_validated_file_extension()
    file_extension = ".jpg"
    image.save("./expected_filter_results/" + name_of_file + file_extension)
    print("Image saved in " + name_of_file + file_extension)
    image.show()


def get_validated_file_extension():
    """Returns a string of a image file extension. Standard file is .jpg
    """

    file_extension = ".jpg"
    repeat = True
    while (repeat):
        file_extension = input("Enter the file extension to save as (e.g.: .jpg): ")
        file_extension = file_extension.lower()

        if ("." not in file_extension):
            repeat = True
        elif (not is_valid_file_extension(file_extension)):
            repeat = True
        else:
            repeat = False

    return file_extension


def is_valid_file_extension(file_extension):
    """Returns True if and only file_extension is a supported
    file extension
    """

    is_true = (file_extension == ".jpg" or file_extension == ".png" 
    or file_extension == ".icns" or file_extension == ".j2p" 
    or file_extension == ".ico" or file_extension == ".j2x" 
    or file_extension == ".im" or file_extension == ".msp" 
    or file_extension == ".jpx" or file_extension == ".pcx")

    return is_true


def get_average_tuple(list_of_tuples):
    """Return the average tuple from the list_of_tuples
    """

    sum_0 = 0
    sum_1 = 0
    sum_2 = 0

    for i in range(len(list_of_tuples)):
        sum_0 += list_of_tuples[i][0]
        sum_1 += list_of_tuples[i][1]
        sum_2 += list_of_tuples[i][2]

    avg_0 = sum_0 / 9
    avg_1 = sum_1 / 9
    avg_2 = sum_2 / 9

    return (round(avg_0), round(avg_1), round(avg_2))


def get_image_data(image):
    """Return a list of pixels from image
    """
    
    return list(image.getdata())


def print_grid(lst, width):
    """Print out lst into a grid given width of desired grid
    """

    for i in range(0, len(lst), width):
        print(lst[i:i+width])

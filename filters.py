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
    image.putdata(data)
    image.save("output.jpg")
    print("Image saved in output.jpg")
    image.show()


def green_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] = round(current_tuple[0]*0.3)
        current_tuple[1] = round(current_tuple[1]*0.59)
        current_tuple[2]= round(current_tuple[1]*0.11)
        data.append(tuple(current_tuple))
    image.putdata(data)
    image.save("output.jpg")
    print("Image saved in output.jpg")
    image.show()


def green_filter(image):
    data = []
    image_data = list(image.getdata())
    for i in range(len(image_data)):
        current_tuple = list(image_data[i])
        current_tuple[0] = round(current_tuple[0]*0.3)
        current_tuple[1] = round(current_tuple[1]*0.59)
        current_tuple[2]= round(current_tuple[1]*0.11)
        data.append(tuple(current_tuple))
    image.putdata(data)
    image.save("output.jpg")
    print("Image saved in output.jpg")
    image.show()



def convert_list_to_2d_list(image, image_data):
    size_of_image = image.size

    grid = []
    count = 0
    for i in range(size_of_image[1]):
        list_of_width_tuples = []
        for j in range(size_of_image[0]):
            list_of_width_tuples.append(image_data[count])
            count += 1
        grid.append(list_of_width_tuples)
    return grid


def convert_2d_list_to_list(image):
    return image.getdata()


def footer(image, data, name_of_file):
    image.putdata(data)
    image.save(name_of_file + ".jpg")
    print("Image saved in " + name_of_file + ".jpg")
    image.show()
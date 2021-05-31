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


def get_average_tuple(list_of_tuples):
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
    return list(image.getdata())

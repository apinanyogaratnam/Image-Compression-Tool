def footer_without_data(image, name_of_file):
    image.save(name_of_file + ".jpg")
    print("Image saved in " + name_of_file + ".jpg")
    image.show()


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


def print_grid(lst, width):
    for i in range(0, len(lst), width):
        print(lst[i:i+width])


def fill_list_indexes(length):
    """Returns a list of indexes up to but not
    including length
    """

    lst = []
    for i in range(length):
        lst.append(i)
    
    return lst


def get_list_of_tuple_indexes(lst, n_dimension, width):
    """Returns a list of items with items in their box form
    """
    
    lst = lst[:n_dimension]
    list_of_indexes = []
    for i in range(n_dimension):
        current_list_indexes = lst[:n_dimension]
        for j in range(len(current_list_indexes)):
            list_of_indexes.append(current_list_indexes[j])
        
        for k in range(n_dimension):
            lst[k] += width

    return list_of_indexes

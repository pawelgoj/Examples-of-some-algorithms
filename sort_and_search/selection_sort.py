def sort(list):

    sort_list = []

    while list != []:
        index = find_smallest_value(list)
        sort_list.append(list.pop(index))

    return sort_list


def find_smallest_value(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if smallest > list[i]:
            smallest = list[i]
            smallest_index = i
    
    return smallest_index


list = [35, 10, 2, 1, 5, 7, 8 , 9 ,9]

list = sort(list)

print(list)



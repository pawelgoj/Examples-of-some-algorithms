
def sum_func(list):
    if list == []: #base case
        return 0
    else: #recursive case
        item = list.pop()
        item = item + sum_func(list)
        return item


def count_elements(list):
    if list == []:
        return 0
    else:
        return 1 + count_elements(list[1:])


def find_max_number(list):
    if list == []:
        return None
    else:
        new_1 = list.pop()
        if len(list) != 1:
            new_2 = list[0]
            if new_1 > new_2:
                list[0] = new_1
            find_max_number(list)
        return list[0]


def find_max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]

    max_f = find_max(list[1:])
    return list[0] if list[0] > max_f else max_f

        


list = [20 , 30, 40 , 50]

print(sum(list))

print(count_elements(list))


list = [20, 40 ,70 , 1, 200]

print(find_max_number(list))
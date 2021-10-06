list = (2, 5, 10, 25, 30, 50)

def binary_search(list, item): 
    min = 0 
    max = len(list) - 1
    while min <= max:
        mid = int((min + max) / 2)

        if list[mid] == item:
            return mid
        elif list[mid] > item:
            max = mid - 1
        elif list[mid] < item:
            min = mid + 1
    return None

item_position = binary_search(list, 9)

print(item_position)

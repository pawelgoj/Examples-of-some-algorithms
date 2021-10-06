
#In sorting it is very important to choose a pivot, it should be chosen randomly. 
#This cease is simplified and we select the first element from the list.
def fast_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [item for item in list[1:] if item <= pivot]
        highter = [item for item in list[1:] if item > pivot]
        return fast_sort(less) + [pivot] + fast_sort(highter)


list =[3, 4, 60, 20, 30]
list = fast_sort(list)

print(list)
# -----------------------------------------------------------
#Example of dynamic programing 
#(C) 2021 Paweł Goj, PL
# Released under MIT license
# -----------------------------------------------------------


import json
import numpy as np

#Read item list from json file. items have a given value and occupy a certain space
with open('items.json', 'r') as file:
    file = file.read()

items = json.loads(file)


'''The function selects the most valuable items that can occupy a certain space.
the dynamic programming technique was used to solve the problem'''
def chose_the_most_valuable_items(items, inventory_space: float, the_lowest_space: float):

    if inventory_space % the_lowest_space != 0:
        raise Exception('Inventory is not divisible by the_lowest_space!!!!')

    #Creates a starting table for calculations
    table = create_table(items, inventory_space)

    row_of_table = 0
    item_list = []

    for item in items.items():

        item = Item(item)
        space = the_lowest_space
        item_list.append(item)
        item_list = sort_by_value(item_list)


        for i in range(0, table.shape[1]):
            if row_of_table > 0 and table[row_of_table-1, i] != None:
                table[row_of_table, i] = table[row_of_table-1, i].copy()

            if item.check_item_will_fit(space) == True:

                if table[row_of_table, i] != None and item.check_items_in_cell_have_bigger_value_than_item(table, row_of_table, i)\
                    and comper_sum_of_values(table[row_of_table, i], table[row_of_table, i-1]):
                    pass

                elif i > 0 and item.check_items_in_cell_have_bigger_value_than_item(table, row_of_table, i-1):
                    table[row_of_table, i] = table[row_of_table, i-1].copy()

                else:
                    table[row_of_table, i] = [item]

                items_in_the_current_cell = table[row_of_table, i]
                items_in_the_current_cell_space = [item.space for item in items_in_the_current_cell]
                sub_space = space - sum(items_in_the_current_cell_space)

                if sub_space > 0:

                    for item_in_item_list in item_list:

                        if item_in_item_list.check_item_will_fit(sub_space) == True and\
                            not item_in_item_list in items_in_the_current_cell:

                            items_in_the_current_cell.append(item_in_item_list)
                            sub_space = sub_space - item_in_item_list.space

                        if not sub_space > 0:
                            break 
          
            space += the_lowest_space

        row_of_table+=1 

    return table

#Create initial table
def create_table(items, inventory_space):
    size = len(items)
    table = np.empty((size, inventory_space), dtype='O')

    return table

#sorts the list with items
def sort_by_value(item_list):

    def func(item):

        return item.get_item_value()

    item_list.sort(key=func, reverse = True)

    return item_list


class Item:
    '''A class representing a single item of appropriate size and value'''

    def __init__(self, item):
        self.name = str(item[0])
        values = item[1]
        self.value = int(values["value"])

        #space occupied by the object
        self.space = int(values["space"])


    def check_item_will_fit(self, size):
        if self.space <= size:
            return True
        else:
            return False


    def get_item_value(self):
        return self.value

    def check_items_in_cell_have_bigger_value_than_item(self, table, row_of_table, i):
        if i < 0: 

            return False

        else:
            items_in_cell = table[row_of_table, i]
            if items_in_cell == None:
                sum_of_items_in_cell = 0

            else:
                sum_of_items_in_cell=0
                for item in items_in_cell:
                    sum_of_items_in_cell+=item.get_item_value()

        if sum_of_items_in_cell < self.get_item_value():
            return False 

        else:
            return True 


def comper_sum_of_values(list1: list, list2: list):
    if list1 != None:
        value1 = [item.get_item_value() for item in list1]
        value1 = sum(value1)

    else:
        value1 = 0

    if list2 != None: 
        value2 = [item.get_item_value() for item in list2]
        value2 = sum(value2)

    else:
        value2 = 0

    if value1 > value2:

        return True
    else:

        return False


table = chose_the_most_valuable_items(items,5, 1)


row = table.shape[0] - 1
col = table.shape[1] - 1
the_best_choice = table[row, col]
table.shape[1]

items = [item.name for item in the_best_choice]
value = [item.get_item_value() for item in the_best_choice]
space = [item.space for item in the_best_choice]

sum_value = sum(value)
sum_space = sum(space)


print('The best choice:', 'items:', items, '\n', 'space of item:', space, ', sum of item spaces:',\
    sum_space, ', value of item:', value, ', sum of item values:', sum_value)


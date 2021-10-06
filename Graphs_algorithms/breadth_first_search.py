# -----------------------------------------------------------
#Example of breadth first search 
#(C) 2021 Paweł Goj, PL
# Released under MIT license
# -----------------------------------------------------------


from collections import deque #list-like container with fast appends and pops on either end
import json


#load a file with the graph
with open('non_weighted_graph.json', 'r') as file:
    file = file.read()

graph = json.loads(file)


#breadth first search implementation 
def find_node(node, start_node):
    if is_looking_for_node(node, start_node):

        return True, 0

    node_looking_for = node
    neighbors = graph[start_node]
    queue= deque([])
    queue += neighbors
    level = {}

    for item in neighbors:
        level.update({item: 1})

    check_list = []

    while queue != deque([]):
        
        node = queue.popleft()

        if not (node in check_list):

            if is_looking_for_node(node, node_looking_for):

                return True, level[node]

            else:
                check_list.append(node)
                neighbors = graph[node]
                queue += neighbors
                level_Of_parent = level[node]

                for item in neighbors:
                    level.update({item: level_Of_parent +1}) 

    return False 


def is_looking_for_node(node, looking_for_node):

    if looking_for_node == node:

        return True

    else:

        return False


#Find way from 'H' to 'Z' 
print('Node exist True/False and the shortest distance between nodes: ',  find_node('Z', 'H'))




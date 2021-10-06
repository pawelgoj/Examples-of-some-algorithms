# -----------------------------------------------------------
#Example of dijkstra algorithm implementation
#(C) 2021 Paweł Goj, PL
# Released under MIT license
# -----------------------------------------------------------


from collections import deque #list-like container with fast appends and pops on either end
import json

#load a file with the graph
with open('Weighted_graph.json', 'r') as file:
    file = file.read()

graph = json.loads(file)


#function creates tuple of dictionary with costs and parents 
def create_costs_and_parents(graph: dict, start_node: str) -> tuple:
    infinity = float("inf")
    costs = {}
    parents = {}
    check_list = []
    try:
        children = graph[start_node]
        check_list.append(start_node)
    except:
        return {}, {}

    if children == 0:
        return {}, {}

    else:
        queue = deque([])
        for key, value in children.items():
            costs.update({key: value})
            parents.update({key: start_node})
            queue += key
            check_list += key
 
        while  queue != deque([]):
            node = queue.popleft()
            children = graph[node]
            if children != {}:
                for key in children.keys():
                    if not key in check_list:
                        costs.update({key: infinity})
                        parents.update({key: None})
                        queue += key
        return costs, parents


def update_costs_list_dijkstra_algorithm(graph: dict, costs: dict) -> tuple:
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for key in neighbors.keys():
            new_cost = cost + neighbors[key]
            if costs[key] > new_cost: 
                costs[key] = new_cost
                parents[key] = node
        
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return costs, parents


def find_lowest_cost_node(costs: dict, processed: list):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for key, value in costs.items():
        if value < lowest_cost and not key in processed:
            lowest_cost = value 
            lowest_cost_node = key
    return lowest_cost_node


#call a function that creates initial tables 
costs, parents = create_costs_and_parents(graph, 'A')


#print tables before use dijkstra algorithm 
print('Initial Tables')
print('Parents {node: parent}: ', parents)
print('Costs:', costs, '\n')


#call the function with implent dijkstra algorithm 
lowest_costs, parents = update_costs_list_dijkstra_algorithm(graph, costs)


#Find the shortest way from A node to G node 
node = 'G'
way = ['G']
while node != 'A':
    node = parents[node]
    way.append(node)

way = way[::-1]


#print tables after use dijkstra algorithm 
print('End Tables')
print('Way:', way)
print('Lowest costs:', lowest_costs)
print('Parents {node: parent}: ', parents)






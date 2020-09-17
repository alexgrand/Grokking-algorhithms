graph = {}
graph['book'] = {}
graph['book']['lp'] = 5
graph['book']['poster'] = 0

graph['lp'] = {}
graph['lp']['drums'] = 20
graph['lp']['guitar'] = 15

graph['poster'] = {}
graph['poster']['drums'] = 35
graph['poster']['guitar'] = 30

graph['drums'] = {}
graph['drums']['piano'] = 10

graph['guitar'] = {}
graph['guitar']['piano'] = 20

graph['piano'] = {}

infinity = float('inf')

costs = {}
costs['lp'] = 5
costs['poster'] = 0
costs['guitar'] = infinity
costs['drums'] = infinity
costs['piano'] = infinity

parents = {}
parents['lp'] = 'book'
parents['poster'] = 'book'
parents['piano'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    
    return lowest_cost_node

def find_shortest_way(parents):
    # now find the backward way from 'piano' to the 'book' in parents
    shortest_way = []
    node = 'piano'

    while node in parents:
        shortest_way.append(parents[node])
        node = parents[node]
    
    shortest_way = shortest_way[::-1]
    shortest_way.append('piano')

    return shortest_way

def dijkstra_search(graph, costs, parents):
    node = find_lowest_cost_node(costs)
    
    while node is not None:
        cost = costs[node]
        neighbors = graph[node] 
        
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            
            if costs[n] > new_cost: 
                costs[n] = new_cost
                parents[n] = node            
        
        processed.append(node)
        node = find_lowest_cost_node(costs)
    
    return find_shortest_way(parents)


shortest_way = dijkstra_search(graph, costs, parents)
print(f"Самый короткий и дешевый путь для обмена книги на пианино для Рамы составляет: {shortest_way} и будет стоить ему ${costs['piano']}")

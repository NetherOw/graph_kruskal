from numpy import random
import datetime
import csv

class weighted_graph:
    def __init__(self, nodes):
        self.graph = []
        self.nodes = nodes
      #chatgpt start
    def __iter__(self): # робимо клас ітерованим, щоб сортувати ребра
        for edge in self.graph:
            yield edge
    #chatgpt end
    def __str__(self): #просто щоб
        return str(self.graph) 
    def add_edge(self, node1, node2, weight):
        self.graph.append([node1, node2, weight])
        self.graph.append([node2, node1, weight])

def graph_generator(graph, density):
    for i in range(len(graph.nodes)):
        for j in range(i, len(graph.nodes)):
            if graph.nodes[i] == graph.nodes[j]:
                pass
            else:
                weight = int(random.choice([x for x in range(max_weight)], p=[1-density]+[density/(max_weight-1)]*(max_weight-1)))
                if weight:
                    graph.add_edge(graph.nodes[i], graph.nodes[j], weight)
    return graph

def shit_to_dict(graph): #Для зручного представлення графу у вигляді списків суміжності
    result = dict()
    for x in graph.nodes:
        result[x] = {}
    for x in graph:
        if x[2]!=0:
            result[x[0]][x[1]] = x[2]
    return result

def find(parent, node): 
    if parent[node]==node:
        return node
    return find(parent, parent[node])
    
def union(parent, rank, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    if rank[root1]>rank[root2]:
        parent[root2] = root1
    elif rank[root2]>rank[root1]:
        parent[root1]= root2
    else:
        parent[root2] = root1
        rank[root1]+=1

def kruskal_algorythm(graph):
    sorted_edges = sorted(graph, key = lambda edge: edge[2])
    parent = [i for i in range(len(graph.nodes))]
    rank = [0]*len(graph.nodes)
    spanning_tree = weighted_graph(graph.nodes)
    for i in range(0, len(sorted_edges), 2):
        parent_node1 = find(parent, sorted_edges[i][0])
        parent_node2 = find(parent, sorted_edges[i][1])
        if parent_node1!=parent_node2:
            spanning_tree.add_edge(sorted_edges[i][0],sorted_edges[i][1],sorted_edges[i][2])
            spanning_tree.add_edge(sorted_edges[i][1],sorted_edges[i][0],sorted_edges[i][2])
            union(parent, rank, parent_node1, parent_node2)
    return spanning_tree

with open('runtime.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['nVertices']+['density']+['runtime'])

number_of_nodes = 200
density = 0.9
max_weight = 10
runtimee =[]
# for i in range(10,201,10):
#     for j in range(10,101,5):
#         edges = graph_generator(weighted_graph([x for x in range(i)]), j/100)    
#         starttime = datetime.datetime.now()
#         minimum_spanning_tree = kruskal_algorythm(edges)
#         endtime = datetime.datetime.now()
#         runtime = (endtime-starttime).total_seconds()
#         print([i,j/100, runtime])

for i in range(10,201,10):
    for j in range(10,101,5):
        for k in range(20):
            edges = graph_generator(weighted_graph([x for x in range(i)]), j/100)    
            starttime = datetime.datetime.now()
            minimum_spanning_tree = kruskal_algorythm(edges)
            endtime = datetime.datetime.now()
            runtimee.append((endtime-starttime).total_seconds()*1000)
        runtime = sum(runtimee)/20
        runtimee = []
        print("writing", i, j/100)
        with open('runtime.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            spamwriter.writerow([i, j/100, runtime])
        
print(1)


    # print(shit_to_dict(edges))
    # print(shit_to_dict(minimum_spanning_tree))

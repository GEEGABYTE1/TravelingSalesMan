import random
from random import randrange
from Graph import Graph
from Vertex import Vertex

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g


def visit_checker(graph):
    for status in list(graph.values()):
        if status == "unvisited":
            return False 
        else:
            continue 
    
    return True  

def traveling_salesperson(graph):
    graph = graph.graph_dict
    final_path = ""
    
    dictionary = {}
    vertices = list(graph.keys())
    
    for i in vertices:
        dictionary[i] = "unvisited"
    
    current_vertex = random.choice(vertices)
    dictionary[current_vertex] = "visited"
    final_path += current_vertex

    vertices_checker = visit_checker(dictionary)

    if vertices_checker != True:
        while vertices_checker == False:
            unvisited_edges = graph[current_vertex].edges
            
            next_vertex_checker = False

            next_vertex = ""

            while next_vertex_checker == False:
                if len(list(unvisited_edges.keys())) == 0:
                    break 
                else:
                    
                    # Minimum Edge 
                    weights = list(unvisited_edges.values())
                    min_weight = min(weights)
                    min_edge = None
                    for neighbour, weight in unvisited_edges.items():
                        if weight == min_weight:
                            min_edge = neighbour
                            break 
                    
                    # Check if the min weight points to a vertex that has been not visited
                    min_edge_edges = list(graph[min_edge].edges.keys())
                    
                    for vertex in min_edge_edges:
                        if dictionary[vertex] == "unvisited":
                            next_vertex += vertex
                            next_vertex_checker = True 
                            break
                        else:
                            continue 
                    
                    if next_vertex_checker == True:
                        break
                    else:
                        unvisited_edges.pop(min_edge)
        
            if len(list(unvisited_edges.keys())) == 0:
                vertices_checker = True 
            else:
                current_vertex =  next_vertex
                dictionary[current_vertex] = 'visited'
                final_path += " -> " + next_vertex 
                vertices_checker = visit_checker(dictionary)
        
    
    print("Final Path: {}".format(final_path))




            
                    
                    







graph = build_tsp_graph(True)

print(traveling_salesperson(graph))
        


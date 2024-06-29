from All_Graph import All_Graph
from Node import Node

# Prints the traversing path
def print_path(path:list):
  
    #Takes a node list as argument. 
   # Prints the fomrated note list.
    
    path_str = [str(p) for p in path]
    print('->'.join(path_str)) 

# A node may have several desitnation nodes. We do not explore the nodes that were visited.
# This function finds all unvisited destiniation nodes.
def find_all_unvisited_destination_nodes(graph:All_Graph, node:Node, visited:set) -> list:
    '''
    Takes a digraph, node and a list of visited nodes as arguments. 
    Returns all destination nodes that are not in the visited list.
    '''
    return [dest for dest in graph.dests_of(node) if dest not in visited]
def find_all_visited_destination_nodes(graph:All_Graph, node:Node, visited:set) -> list:
    '''
    Takes a digraph, node and a list of visited nodes as arguments. 
    Returns all destination nodes that are not in the visited list.
    '''
    return [dest for dest in graph.dests_of(node) if dest in visited]
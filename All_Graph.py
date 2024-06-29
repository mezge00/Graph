import numpy as np
import os
import sys
from Node import Node
from Edge import Edge

class All_Graph:
    def __init__(self):
        self._nodes=list()
        self._edges=dict()
       # self.mark_color=dict()
        
    def dests_of(self, node):
        '''
        Takes a node as argument. Return a a list of destination nodes
        '''
        if node not in self._nodes:
            raise ValueError('The node is not in the Digraph.')
        else:
            return self._edges[node]
    def addNode(self,node):
        if node in self._nodes:
            raise valueError('Node already exists')
        else:
            self._nodes.append(node)
            self._edges[node]=list()
    
    def addEdge(self,edge):
        if edge.src not in self._nodes:
            raise valueError('Node has no source')
        elif edge.dest not in self._nodes:
            raise valueError('Node has no destination node')
        else:
            self._edges[edge.src].append(edge.dest)
       
    def has_node(self,node):
        if node not in self._nodes:
            return True
        else:
            return False
  
       
    '''  def add_color(self,color):
        self.mark_color[edge.src].append(edge.dest)
    def display(self):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[i][j],end=' ')
            print(' ')'''
   
    def __repr__(self):
        '''Computes the “official” string representation of an object. 
        This is the representation printed by the shell when evaluating the object.
        '''
        # Makes a flat list out of a list of lists to get all desitinations in the Digraph
        dest_list = [dest for sublist in self._edges.values() for dest in sublist]
        # Uses Pythin f-string to format output
        # Uses __name__ attribute of the class to get the class name
        return f"{type(self).__name__}(Nodes:{len(self._nodes)}, Edges:{len(dest_list)})"

    # Overloading __str__, creates a pretty string representation of an object
    def __str__(self):
        '''
        Computes the pretty string representation of an object. 
        This is the representation printed by the print() statement.
        '''
        rtn_value = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                rtn_value = rtn_value + src.name + '->' + dest.name + '\n'
        return rtn_value[:-1]

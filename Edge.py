class Edge:
    def __init__(self,src,dest):
        self._src=src
       # self.cost=cost
        self._dest=dest
        
    @property
    def src(self):
        return self._src
    @property
    def dest(self):
        return self._dest
  #  @property
    #def cost(self):
       # return self.cost
   # Overloading __repr__, creates a canconical string represents an object
    def __repr__(self):
        '''
        Computes the “official” string representation of an object. 
        This is the representation printed by the shell when evaluating the object.
        '''
        # Uses Pythin f-string to format output
        # Uses __name__ attribute of the class to get the class name
        return f"{type(self).__name__}({self._src}->{self._dest})"

    # Overloading __str__, creates a pretty string representation of an object
    def __str__(self):
        '''
        Computes the pretty string representation of an object. 
        This is the representation printed by the print() statement.
        '''
        # Uses __name__ attribute of the class to get the class name
        return f"{self._src} -> {self._dest}"
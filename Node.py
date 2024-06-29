class Node:
    def __init__(self,Data):
        self.data=Data
    @property
    def Data(self):
        return self.data

 #Overloading __repr__, creates a canconical string represents an object
    def __repr__(self):
        '''
        Computes the “official” string representation of an object. 
        This is the representation printed by the shell when evaluating the object.
        '''
        # Uses Python f-string to format output
        # Uses __name__ attribute of the class to get the class name
        return f"{type(self).__name__}({self.data})"

    # Overloading __str__, creates a pretty string representation of an object
    def __str__(self):
        '''
        Computes the pretty string representation of an object. 
        This is the representation printed by the print() statement.
        '''
        return self.data
    '''''def __eq__(self, other):
        return (self.Data) == (other.Data)

    def __hash__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)'''''
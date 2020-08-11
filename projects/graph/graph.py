"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        """ Use dictionary to hold vertices"""
        self.vertices = {}

    def add_vertex(self, vertex):
        """ Add a vertex. Input vertex as key, values are a set of neighbour vertices """
        self.vertices[vertex] = set()       

    def add_edge(self, v1, v2):
        """ Add a directed edge to the graph.
        Add v2 to the set of neighbour vertices of v1 """
        # make sure vertices are already in the graph before connecting
        if v1 in self.vertices and v2 in self.vertices:
            # establish an edge from v1 to v2 implicitedly
            self.vertices[v1].add(v2) 
        else:
            raise IndexError("Nonexist vert")        

    def get_neighbors(self, vertex):
        """ Get all neighbors vertices of a vertex. """
        return self.vertices[vertex]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empyt queue to store front vertices (neighbors of visited vertices
        q = Queue()
        # Create a set to store visited vertices
        visited = set()
        # init: enqueue to starting node
        q.enqueue(starting_vertex)
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first item
            v = q.dequeue()
            # if it is not visited
            if v not in visited:
                # add to set visited
                visited.add(v)
                print(f"{v},", end=" ")

                # add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
            # if it is visited, do nothing
  

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack to store front vertices
        s = Stack()
        # Created visited to store visited vertices
        visited = set()
        # add to front stack
        s.push(starting_vertex)
        # if stack not exhausted
        while s.size() > 0:
            # pop the top vertex and check if it has been visited
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(f"{v},", end=" ")
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def bfs(self, starting_vertex, destination_vertex):
        """ Breath First Search:
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue to queue up list: [[path1], [path2], ...]
        q = Queue()
        # enqueue A PATH to the starting vertex
        path = [starting_vertex]
        q.enqueue(path)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empyt:
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]
            # if that vertex has not been visited
            if v not in visited:
                # Check if it is the destination
                if v == destination_vertex:
                    # if so, return PATH
                    return path
                # add it to the visited set
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    # copy the PATH 
                    new_path = list(path)
                    # append the neighbor to the back of the queue
                    new_path.append(next_vert)
                    # add a PATH to its neighbors to the back of the queue
                    q.enqueue(new_path)
        
        # path not find         
        return None                    

                                            
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue to queue up list: [[path1], [path2], ...]
        s = Stack()
        # enqueue A PATH to the starting vertex
        path = [starting_vertex]
        s.push(path)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empyt:
        while s.size() > 0:
            # Dequeue the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            v = path[-1]
            # if that vertex has not been visited
            if v not in visited:
                # Check if it is the destination
                if v == destination_vertex:
                    # if so, return PATH
                    return path
                # add it to the visited set
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    # copy the PATH
                    new_path = list(path)
                    # append the neighbor to the back of the queue
                    new_path.append(next_vert)
                    # add a PATH to its neighbors to the back of the queue
                    s.push(new_path)

        # path not find
        return None
 

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        using recursion, sarting with input vertex.
        """
        if visited == None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex, end=" ")

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                self.dft_recursive(v, visited)


    def dfs_recursive(self, starting_vertex, destination_vertex, path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order. Use recursion.
        """
        # append vertex to path after initial call
        
        path += [starting_vertex]      
        # base case destination already in path 
        if path[-1] == destination_vertex:
            return path

        # otherwise, exhaust all neighbors
        for v in self.get_neighbors(starting_vertex):
            # if neighbor has not been visited, search neighbor resursively add neighbor to path
            if v not in path:
                path = self.dfs_recursive(v, destination_vertex, path)
            return path  
            

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    
  
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("\n")
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    
    graph.dft(1)
    print("\n")
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
    
    print(graph.dfs_recursive(1, 6))

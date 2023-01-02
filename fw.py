from math import inf
from copy import deepcopy

class PathFinder:

    def __init__(self, g):
        self.matrix = g
        self.num_of_vertex = len(g)
        self.distance = list(map(lambda i: list(map(lambda j: j, i)), G))
        self.paths = []
        self.initialize_paths()
        pass

    def floyd_warshall(self):
        # distance = list(map(lambda i: list(map(lambda j: j, i)), G))
        
        # Adding vertices individually
        for k in range(self.num_of_vertex):
            for i in range(self.num_of_vertex):
                for j in range(self.num_of_vertex):
                    # self.distance[i][j] = min(self.distance[i][j], self.distance[i][k] + self.distance[k][j])
                    if (self.distance[i][k] == inf) or (self.distance[k][j] == inf):
                        continue
                    if (self.distance[i][j]) > (self.distance[i][k]+self.distance[k][j]):
                        self.paths[i][j] = self.paths[i][k]
                        self.distance[i][j] = self.distance[i][k] + self.distance[k][j]
        self.print_solution()
        pass

    def initialize_paths(self):
        for _ in range(self.num_of_vertex):
            self.paths.append([0] * len(self.matrix))
        
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                self.distance[i][j] = self.matrix[i][j]
    
                if (self.matrix[i][j] == inf):
                    self.paths[i][j] = -1
                else:
                    self.paths[i][j] = j


    # Printing the solution
    def print_solution(self):
        print("DISTANCES")
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                if(self.distance[i][j] == inf):
                    print("INF", end=" ")
                else:
                    print(self.distance[i][j], end="  ")
            print(" ")

        print("PATHS")
        
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                if(self.paths[i][j] == inf):
                    print("INF", end=" ")
                else:
                    print(self.paths[i][j], end="  ")
            print(" ")

    def gen_path(self, start, end):

        pass


if __name__ == "__main__":
    
    G = [[0,2,inf,2,1,inf,inf,inf,inf,inf,inf,inf,inf,inf],
        [2,0,inf,inf,2,3,inf,inf,inf,inf,inf,inf,inf,inf],
        [inf,2,0,inf,inf,1,4,inf,inf,inf,inf,inf,inf,inf],
        [2,inf,inf,0,4,inf,inf,3,inf,inf,6,inf,inf,inf],
        [1,2,inf,4,0,3,inf,5,1,inf,inf,inf,inf,inf],
        [inf,3,1,inf,3,0,3,inf,2,2,inf,inf,inf,inf],
        [inf,inf,4,inf,inf,3,0,inf,inf,5,inf,inf,inf,inf],
        [inf,inf,inf,3,5,inf,inf,0,1,inf,1,1,inf,inf],
        [inf,inf,inf,inf,1,2,inf,1,0,3,inf,5,1,inf],
        [inf,inf,inf,inf,inf,2,5,inf,3,0,inf,inf,2,1],
        [inf,inf,inf,6,inf,inf,inf,1,inf,inf,0,2,inf,inf],
        [inf,inf,inf,inf,inf,inf,inf,1,5,inf,2,0,2,inf],
        [inf,inf,inf,inf,inf,inf,inf,inf,1,2,inf,2,0,inf],
        [inf,inf,inf,inf,inf,inf,inf,inf,inf,1,inf,inf,4,0]
        ]
    pf = PathFinder(G)
    pf.floyd_warshall()
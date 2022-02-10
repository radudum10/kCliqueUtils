import sys
import itertools


def get_vertex_degree(vertex):
    degree = 0
    for i in matrix[vertex]:
        if i:
            degree += 1

    return degree


# Take each vertex and check if it's connected to the others
def check_completeness(vertex_tuple):
    for edge in itertools.combinations(vertex_tuple, 2):
        i = edge[0]
        j = edge[1]
        if matrix[i-1][j-1] == 0:
            return False

    return True


# Open and read the file
file = open(sys.argv[1], 'r')
Lines = file.readlines()

k = int(Lines[0])  # clique size
num_of_vertices = int(Lines[1])
num_of_edges = int(Lines[2])

# Build the adjacency matrix
matrix = [[0 for i in range(num_of_vertices)] for j in range(num_of_vertices)]

for i in range(num_of_edges):
    indices = Lines[i + 3].split(" ")
    row = int(indices[0])
    column = int(indices[1])
    # indexing starts from 0, must subtract
    matrix[row - 1][column - 1] = 1
    matrix[column - 1][row - 1] = 1

# Create a list with all elements that can form a clique with that size
vertices_list = []
for i in range(num_of_vertices):
    if get_vertex_degree(i) >= (k - 1):
        vertices_list.append(i+1)

# Generate subsets of k elements and check if there is a complete subgraph
for subset in itertools.combinations(vertices_list, k):
    if check_completeness(subset):
        print(True)
        exit()

print(False)


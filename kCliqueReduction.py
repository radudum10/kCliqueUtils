import sys


# Open and read the file
file = open(sys.argv[1])
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

ans = ""

# Clique should have a vertex on each position
for u in range(1, k+1):
    clause = "("
    for i in range(1, num_of_vertices+1):
        clause += "x" + str(i) + str(u)
        if i < num_of_vertices:
            clause += " V "

    clause += ") ^ "
    ans += clause

# Clique can't contain a vertex multiple time (the i-th vertex can't be the j-th vertex)
for u in range(1, num_of_vertices + 1):
    for i in range(2, k+1):
        for j in range(1, i):   # in order to not repeat clauses
            clause = "(~x" + str(u) + str(i) + " V ~x" + str(u) + str(j) +\
                     ") ^ "
            ans += clause

# Taking all edges from the complement graph and if there is an edge that is formed by
# 2 vertices that are in the actual clique, then the clique is invalid (it doesn't contain an edge
# between that 2 nodes)

for u in range(2, k+1):
    for v in range(1, u):
        for i in range(1, num_of_vertices+1):
            for j in range(1, num_of_vertices+1):
                if (i == j) or (matrix[i - 1][j - 1] == 1):
                    continue
                clause = "(~x" + str(i) + str(u) + " V ~x" + str(j) + str(v) + ") ^ "
                ans += clause

ans = ans[:-3]  # removing the " ^ " from the end of the string
print(ans)


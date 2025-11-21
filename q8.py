#Create a 3x3 list of lists with random values and normalize it.

import random
matrix = [[random.randint(0, 10) for x in range(3)] for x in range(3)]
mean = sum(sum(row) for row in matrix)/9
std = (sum((x-mean) **2 for row in matrix for x in row)/9) ** .5
normalized = [[(x-mean) / std for x in row] for row in matrix]
print(normalized)
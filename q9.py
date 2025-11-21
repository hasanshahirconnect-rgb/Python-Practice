#Calculate the sum of the diagonal elements of a 3x3 matrix (list of lists).

import random
lst = [[random.randint(0, 10) for x in range(3)] for x in range(3)]
diagnol = sum(lst[i][i] for i in range(3))
print(diagnol)
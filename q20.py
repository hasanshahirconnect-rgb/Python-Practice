# Find the mean of each row in a 2D list.
import random
array = [[random.randint(0, 10) for x in range(3)] for y in range(3)]
all_means = []
for row in range(3):
    sum = 0
    for col in range(3):
        sum += array[row][col]
    all_means.append(sum/3)
print(all_means)



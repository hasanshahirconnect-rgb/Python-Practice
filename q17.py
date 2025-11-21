#Find the index of the maximum value in a list.
import random
max = 0
lst = [random.randint(0,10) for x in range(10)]
for item in lst:
    if item > max:
        max = item
print(max)

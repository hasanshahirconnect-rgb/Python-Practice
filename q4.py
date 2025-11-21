#Extract all odd numbers from a list of integers.

lst = list(range(10))
odd = [x for x in lst if x%2 != 0]
print(odd)
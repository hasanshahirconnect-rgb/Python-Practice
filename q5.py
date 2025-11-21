# Replace all odd numbers in a list with -1.

lst = list(range(10))
odd = [-1 if x%2 != 0 else x for x in lst]
print(odd)
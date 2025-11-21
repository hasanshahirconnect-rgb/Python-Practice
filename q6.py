#Convert a list of integers to a list of booleans where all non-zero values become True.

lst = list(range(10))
boolean = [bool(x) for x in lst]
print(boolean)
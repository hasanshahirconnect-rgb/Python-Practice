#Replace all even numbers in a list with their negative.

lst = list(range(10))
lst = [x*-1 if x%2 == 0 else x for x in lst]
print(lst)
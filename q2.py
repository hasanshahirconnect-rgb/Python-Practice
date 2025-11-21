# Convert a list of integers to a list of strings.
#lst = [str(lst[x]) for x in lst]

lst = list(range(10))
str_lst = list(map(str, lst))
print(str_lst)
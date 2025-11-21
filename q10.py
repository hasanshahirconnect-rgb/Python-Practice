#Find the indices of non-zero elements in a list.

lst = list(range(10))
non_zero_indices = [i for i, x in enumerate(lst) if x != 0]
print(non_zero_indices)

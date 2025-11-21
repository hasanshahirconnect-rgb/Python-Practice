#Get the common items between two lists.

import random
list1 = [random.randint(0,10) for x in range(10)]
list2 = [random.randint(0,10) for x in range(10)]
common = list(set(list1) & set(list2))
print(common)
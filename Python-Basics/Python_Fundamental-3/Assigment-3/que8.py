list1 = [1, 2, 3]
list2 = [3, 4]

set1 = set(list1)
set2 = set(list2)

if set1.isdisjoint(set2):
    print("No common elements")
else:
    print("Common elements present")
# Input two lists from user
list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

# Merge lists
result = list1 + list2

# Sort the merged list
result.sort()

print("Sorted merged list:", result)
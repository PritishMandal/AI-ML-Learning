numbers = [1, 2, 3, 2, 4, 5, 1, 6]

duplicates = set()

for i in numbers:
    if numbers.count(i) > 1:
        duplicates.add(i)

print("Duplicate elements:", duplicates)# duplicates isliye set me store kiya hai taki duplicate elements remove ho jaye
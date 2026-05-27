numbers = (1, 2, 3, 4, 5, 6, 7, 8)

even = ()
odd = ()

for i in numbers:
    if i % 2 == 0:
        even = even + (i,)
    else:
        odd = odd + (i,)

print("Even Tuple:", even)
print("Odd Tuple:", odd)
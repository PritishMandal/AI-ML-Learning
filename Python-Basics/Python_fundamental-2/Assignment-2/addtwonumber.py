def print_even(a, b):# ye line print_even function ko define kar rahi hai jo do parameters a aur b leta hai
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)

print_even(2, 10)
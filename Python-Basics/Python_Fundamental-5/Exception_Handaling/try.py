try:
    # User se number input le rahe hain
    x = int(input("enter x:"))

    # 10 ko x se divide kar rahe hain
    ans = 10 / x

# Agar user 0 enter kare to ye exception handle hoga
except ZeroDivisionError:
    print("0 se divide karna allowed nahi hai")

# Agar koi error nahi aaya to answer print hoga
else:
    print(f"answer = {ans}")
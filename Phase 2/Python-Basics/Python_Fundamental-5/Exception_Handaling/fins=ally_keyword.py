try:
    x = int(input("enter x:"))
    ans = 10 / x


except ZeroDivisionError:
    print("0 se divide karna allowed nahi hai")

else:
    print(f"answer = {ans}")
finally:
    print("End of program")
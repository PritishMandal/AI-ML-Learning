username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("login successful!")
elif username != "admin":
    print("wrong username, try again.")
else:
    print("wrong password, try again.")
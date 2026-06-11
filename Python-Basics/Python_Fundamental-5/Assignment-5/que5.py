# LOGIC:
# 1. Try to open the file in read mode
# 2. If the file exists, print the data
# 3. If the file does not exist, handle the exception
# 4. Print "File not found!"

try:
    f = open("data.txt", "r")

    data = f.read()

    print(data)

    f.close()

except FileNotFoundError:

    print("File not found!")


# QUESTION:
# Q5. Write a program that tries to open "data.txt" in read mode.
# If the file does not exist, catch the exception and print "File not found!"
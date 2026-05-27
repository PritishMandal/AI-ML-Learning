f = open("names.txt", "w")# ye line names.txt file ko write mode me khol rahi hai

for i in range(5):
    name = input("Enter name: ")
    f.write(name + "\n")

f.close()

f = open("names.txt", "r")

data = f.read()

print(data)

f.close()


# QUESTION:
# Q1. Create a program that:
# 1. Opens a file "names.txt" in write mode
# 2. Writes 5 names (one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names
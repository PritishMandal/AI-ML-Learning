# LOGIC:
# 1. Open the file in append mode
# 2. Add a new log entry
# 3. Open the file in read mode
# 4. Print all log entries

f = open("log.txt", "a")

f.write("Program run successfully\n")# Ye line log.txt file me add ho jayegi

f.close()

f = open("log.txt", "r")# ye line log.txt file ko read mode me khol rahi hai

data = f.read()

print(data)

f.close()


# QUESTION:
# Q2. Create a program that:
# 1. Opens a file "log.txt" in append mode
# 2. Adds a new log entry
# 3. Opens the file in read mode and prints all logs
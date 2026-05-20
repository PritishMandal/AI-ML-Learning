string = input("Enter a string: ")

unique = set(string)

print("Unique Characters:", unique) # unique characters isliye set me store kiya hai taki duplicate characters remove ho jaye
print("Count:", len(unique))
data = True

with open ("sample.txt", "r") as f:
  while data:
    data = f.readline()
    print(data)
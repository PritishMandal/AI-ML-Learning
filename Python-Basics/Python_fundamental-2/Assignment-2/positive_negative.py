while True:
    n = input("Enter number or Quit: ")

    if n == "Quit":
        break

    n = int(n)

    if n >= 0:
        print("Positive")
    else:
        print("Negative")
secret = 10
while True:
    num  = int(input("Guess the number :"))

    if  num > secret:
      print("To High")

    elif num < secret:
       print("To low")

    else:
      print("correct")
      break

      
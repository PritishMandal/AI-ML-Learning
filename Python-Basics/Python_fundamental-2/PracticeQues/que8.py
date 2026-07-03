def calculator(a,b,operation):

    if operation == '+':
       return a+b
    
    elif  operation == '-':
       return a-b

    elif operation == '*':
       return a*b

    elif operation == '/':
       return a/b
    else :
        return "Invalided"

    
print(calculator(5,4,'-'))


    

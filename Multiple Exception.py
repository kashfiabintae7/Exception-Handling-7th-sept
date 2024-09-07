try:
    num1 = int(input("Ënter a Number: "))
    num2 = int(input("Ënter a Number: "))
    
    result = num1/num2
    
    print("Result is : ", result)
    print("Result is : ", result1)
    
except ZeroDivisionError :
    print("Division by Zero is not allowed.")
    
    
except ValueError:
    print("Please enter a Numerical value.")
    
    
except NameError as ex:
    print("The exception is " ,ex)
          
        
finally: 
    print("I will execute no matter what happens MUHAHAHHAH!!")
    
print("Iam outside EVERYTHING")
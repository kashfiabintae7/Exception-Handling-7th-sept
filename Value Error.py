try :
    num = int(input("Enter your Number: "))
    print(num)
    
    
except ValueError as ex:
    print("Exception: ", ex)
    
    
print("Ïam Outside the Try Block.")
valid = False 

while not valid:
    
    try:
        n = int(input("Enter a Number: "))
        
        if n%2 == 0:
            print("bye BYE.")
            valid = True
            
    except ValueError:
        print("Invalid Data Type.")
        
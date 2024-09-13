def agecounter(ae):
    if ae < 0:
        raise ValueError("The only acceptable numbers are those greater than Zero.")
    
    if ae % 2 == 0:
        print("The age entered is even.:D")
        
    else:
        print("The age entered is odd.;)")
        
        
    try:
        numnum = int(input("Enter the Age you wish: "))
        agecounter(numnum)
        
        
    except ValueError:
        print("Anything ouside Integer Value or smaller than Zero is considered outside function.Try again later;P")
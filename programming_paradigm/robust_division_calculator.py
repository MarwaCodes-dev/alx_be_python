def safe_divide(numerator, denominator) :
    try :
        number = int(input("Enter a number: "))
        print(float(numerator)/float(denominator)) 
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError :
        print("Error: Please enter numeric values only")
        
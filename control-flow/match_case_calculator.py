num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation =input("Choose the operation (+, -, *, /):")
#For addition (+), subtract (-), multiply (*), and divide (/).
match operation:
    case "+":
        print("The result is",num1+num2,".")
    case "*":
        print("The result is",num1*num2,".")    
    case "-":
        print("The result is",num1-num2,".")  
    case "/" if num1 and num2 != 0:
        print("The result is",num1/num2,".") 
    case other:
        print("Cannot divide by zero.")    
       


     






    
          

    
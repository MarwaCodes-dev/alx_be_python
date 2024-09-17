num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation =input(" Choose the operation (+, -, *, /): / ")
#for addition (+), subtract (-), multiply (*), and divide (/).
if operation == "+":
    print("The result is",num1+num2,".")
elif operation == "-":
    print("The result is",num1-num2,".")
elif operation == "*":
    print("The result is",num1*num2,".") 
elif operation =="/":
    if num1 !=0 &num2 !=0:
        print("The result is",num1/num2,".") 
    else:
        print("Cannot divide by zero.")  


    
          

    
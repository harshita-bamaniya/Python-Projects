def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "Error : Cannot divide by zero."
    return a + b

while True:
    
 print("\nSimple Calculator")
 print("+ Addition")
 print("- Subtraction")
 print("* Multiplication")
 print("/ Division")

 choice = input("Enter your choice (+,-,*,/) : ")

 if choice not in ['+','_','*','/']:
    print("Invalid Choice! Please try again")
    continue

 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))

 if choice == "+":
    result = add(num1, num2)
    print("Result",result)

 elif choice == "-":
    result = sub(num1, num2)
    print("Result",result)

 elif choice == "*":
    result = mul(num1, num2)
    print("Result",result)

 elif choice == "/":
    result = div(num1, num2)
    print("Result",result)   

   
    again = input("\nDo you want to continue (yes/no): ") 

    if again.lower() != "yes" :
        print("\nThank you for using the Simple Calculator!")
        break   



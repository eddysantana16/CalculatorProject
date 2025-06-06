def add (a, b): 
    return a + b
def subtract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    if b == 0: 
        return "Cannot Divide By Zero! -_-"
    return a / b 
def main ():
    while True:
        print("--- Simple Calculator ---")
        print("Choose An Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit Application")

        choice = input("Enter your choice (1-5): ")
        if choice == "5":
            print("Goodbye!/Adios!")
            break
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please Enter A Valid Number! -_-")
            continue

        if choice == "1":
            print("Result:", add(num1+num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid Choice. Try again! -_-")
if __name__ == "__main__":
    main()
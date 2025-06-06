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

operations = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide
}
def calculate(choice, num1, num2):
    operations = {
        "1": num1 + num2,
        "2": num1 - num2,
        "3": num1 * num2,
        "4": num1 / num2 if num2 != 0 else "Cannot Divide By Zero! -_-"
    }
    return operations.get(choice, "Invalid Choice. Try again! -_-")

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
        elif choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Please Enter A Valid Number! -_-")
            continue

        if choice == "1":
            print("Result:", add(num1, num2))
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
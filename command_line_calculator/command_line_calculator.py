from services.calculator_service import CalculatorService

def main():
    calculator = CalculatorService()

    print("📟 Welcome to the Python CLI Calculator!")
    print("Available operations: add, subtract, multiply, divide, power")
    print("Type 'exit' to quit.\n")

    while True:
        operation = input("👉 Enter operation: ").strip().lower()

        if operation == "exit":
            print("👋 Exiting calculator. Goodbye!")
            break

        try:
            num1 = float(input("🔢 Enter first number: "))
            num2 = float(input("🔢 Enter second number: "))
            result = calculator.calculate(operation, num1, num2)
            print(f"✅ Result: {result}\n")
        except ValueError as e:
            print(f"❌ Error: {e}\n")
        except Exception:
            print("❌ Something went wrong. Try again.\n")

if __name__ == "__main__":
    main()

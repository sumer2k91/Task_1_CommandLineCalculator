# Python Command Line Calculator

This is a simple, modular Python command-line calculator application built using **SOLID principles**. It supports basic arithmetic operations and is designed to be clean, maintainable, and extendable.

## 🚀 Features

- Addition
- Subtraction
- Multiplication
- Division (with zero-division handling)
- Power
- Command-line interface
- SOLID-structured code (SRP, OCP, etc.)

## 🗂 Project Structure

```
command_line_calculator/
├── command_line_calculator.py        # Entry point
├── interfaces/
│   └── operation.py                  # Abstract base class
├── operations/
│   ├── add.py
│   ├── subtract.py
│   ├── multiply.py
│   ├── divide.py
│   ├── power.py
│   └── __init__.py
├── services/
│   └── calculator_service.py         # Operation manager
```

## 🛠 How to Run

1. Navigate to the project folder:

```bash
cd command_line_calculator
```

2. Run the calculator:

```bash
python3 command_line_calculator.py
```

3. Follow the prompts to perform operations.

## 📦 Requirements

- Python 3.6 or later
- No third-party packages required

## 📄 License

This project is free to use and modify.

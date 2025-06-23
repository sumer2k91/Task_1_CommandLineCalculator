from operations.add import Add
from operations.subtract import Subtract
from operations.multiply import Multiply
from operations.divide import Divide
from operations.power import Power

class CalculatorService:
    def __init__(self):
        self.operations = {
            "add": Add(),
            "subtract": Subtract(),
            "multiply": Multiply(),
            "divide": Divide(),
            "power": Power()
        }

    def calculate(self, operation_name: str, a: float, b: float):
        operation = self.operations.get(operation_name)
        if not operation:
            raise ValueError(f"Unsupported operation '{operation_name}'")
        return operation.execute(a, b)

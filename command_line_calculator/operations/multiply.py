from interfaces.operation import Operation

class Multiply(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b

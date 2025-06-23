from interfaces.operation import Operation

class Subtract(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b

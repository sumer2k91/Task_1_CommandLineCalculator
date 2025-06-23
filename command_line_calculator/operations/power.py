from interfaces.operation import Operation

class Power(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b

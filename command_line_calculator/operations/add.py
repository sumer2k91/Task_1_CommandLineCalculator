from interfaces.operation import Operation

class Add(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b

"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):

    def __init__(self, message="Низкий уровень топлива."):
        self.message = message
        super().__init__(self.message)


class NotEnoughFuel(Exception):
    def __init__(self, message="Не хватает топлива"):
        self.message = message
        super().__init__(self.message)


class CargoOverload(Exception):
    def __init__(self, message="Перегрузка"):
        self.message = message
        super().__init__(self.message)

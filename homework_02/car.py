"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, engine=None):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.engine = engine

    def set_engine(self, engine):
        self.engine = engine

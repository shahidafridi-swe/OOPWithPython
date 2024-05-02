from abc import ABC,abstractmethod

class Vehicle:
    def __init__(self, vehicle_type, lisecne, rate) -> None:
        self.vehicle_type = vehicle_type
        self.lisence = lisecne
        self.rate = rate

class Car(Vehicle):
    def __init__(self, vehicle_type, lisecne, rate) -> None:
        super().__init__(vehicle_type, lisecne, rate)

class Bike(Vehicle):
    def __init__(self, vehicle_type, lisecne, rate) -> None:
        super().__init__(vehicle_type, lisecne, rate)   
        
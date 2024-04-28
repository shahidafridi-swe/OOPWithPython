class Engine:
    def __init__(self) -> None:
        pass
    def start(self):
        return "Engine Started"

class Driver:
    pass

class Wheel:
    pass

# Composition provides "has a" relation


# Car "has a" Engine
# Car "has a" Driver
# Car "has a" Wheel
class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()
        self.wheel = Wheel()

        self.engine.start()

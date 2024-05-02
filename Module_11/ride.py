
from datetime import datetime
from vehicle import Car, Bike

class RideSharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    
    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f"Company Name: {self.company_name} with {len(self.drivers)} driver"

        


class Ride:
    def __init__(self, start_location, end_location, vehicle) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)
        self.vehicle = vehicle

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

        
    def calculate_fare(self, vehicle_type):
        distance = 10
        per_km_fare = {
            'car': 50,
            'bike' : 20
        }
        return distance * per_km_fare.get(vehicle_type)


    def __repr__(self) -> str:
        return f"Ride Details: Started from - {self.start_location} To - {self.end_location}"
    


class RideRequest:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location

    
class RideMatching:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers

    def find_driver(self, ride_request, vehicle_type):
        if len(self.available_drivers) > 0:
            print("Looking Drivers...")
            driver = self.available_drivers[0]
            if vehicle_type == 'car':
                vehicle = Car('car', 'ABC1231', 100)
            elif vehicle_type == 'bike':
                vehicle = Bike('bike', "XYZ789",50)
            ride = Ride(ride_request.rider.current_location, ride_request.end_location,vehicle)

            driver.ride_accept(ride)
            return ride
    


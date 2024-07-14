class Vehicle:
    def __init__(self, vehicle_type, tonnage, volume, fuel_capacity, fuel_consumption):
        self.vehicle_type = vehicle_type
        self.tonnage = tonnage
        self.volume = volume
        self.fuel_capacity = fuel_capacity # litres
        self.fuel_consumption = fuel_consumption # litres/100km


LARGE_TRUCK = Vehicle("LARGE_TRUCK", 20, 100, 500, 40)
MEDIUM_TRUCK = Vehicle("MEDIUM_TRUCK", 15, 50, 450, 35)
SMALL_TRUCK = Vehicle("SMALL_TRUCK", 12, 20, 400, 30)

class Vehicle:
    def __init__(self, vehicle_type, tonnage, volume):
        self.vehicle_type = vehicle_type
        self.tonnage = tonnage
        self.volume = volume


LARGE_TRUCK = Vehicle("LARGE_TRUCK", 20, 100)
MEDIUM_TRUCK = Vehicle("MEDIUM_TRUCK", 15, 50)
SMALL_TRUCK = Vehicle("SMALL_TRUCK", 12, 20)

import simpy

class Driver:
    def __init__(self, env, id, name, licence, vehicle):
        self.env = env
        self.id = id
        self.name = name
        self.licence = licence
        self.vehicle = vehicle
        self.current_location = None
        self.status = "idle"

    def start_route(self, route):
        self.status = "driving"
        self.env.process(self.drive(route))

    def drive(self, route):
        for waypoint in route:
            yield self.env.timeout(waypoint["duration"])
            self.current_location = waypoint["location"]
            print(f"{self.name} is at {self.current_location} at {self.env.now}.")

    def load_product(self):
        self.status = "loading"
        yield self.env.timeout(5)
        print(f"{self.name} has loaded the product at {self.current_location} at {self.env.now}.")

    def unload_product(self):
        self.status = "unloading"
        yield self.env.timeout(5)
        print(f"{self.name} has unloaded the product at {self.current_location} at {self.env.now}.")

    
    
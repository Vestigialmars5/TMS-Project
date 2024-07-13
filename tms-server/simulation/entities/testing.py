import random
import threading
import time

DOCKS = 6
LOADING_TIME = random.randint(1, 5)
UNLOADING_TIME = random.randint(1, 15)
TRAVEL_TIME = random.randint(6, 20)
REORDER_LEVEL = 50
MAX_INVENTORY = 100
INVENTORY_DECREASE_RATE = 10
PRODUCT_TYPES = 10
SIM_TIME = 100
COUNT = 0
DRIVER_WAIT_TIME = dict()


class TimeKeeper:
    def __init__(self, inventories):
        self.time = 0
        self.lock = threading.Lock()
        self.warehouse = self.WarehouseCtrl(inventories, DOCKS)
        self.driver = self.DriverController()

    
    def increment(self):
        while True:
            with self.lock:
                self.time += 1
                print(f'Time: {self.time}')
            time.sleep(1)
            if self.time == SIM_TIME:
                print("Reached simulation time, close all threads.")
                self.send_finish_signal()
                break
    
    def get_time(self):
        return self.time

    def send_finish_signal(self):
        self.warehouse.stop = True
        self.driver.stop = True

    class WarehouseCtrl:
        """
        Will take care of handling the warehouse operations.

        Checking inventory levels, placing requests, managing docks, etc.
        """
        def __init__(self, inventories, docks):
            self.inventories = inventories
            self.reorder_needed = list()
            self.docks = docks
            self.monitor_inventory = threading.Thread(target=self.monitor_inventory).start()
            self.lower_inventories = threading.Thread(target=self.lower_inventories).start()
            self.stop = False

        def monitor_inventory(self):
            while True:
                for product, inventory in self.inventories.items():
                    if inventory.quantity < inventory.reorder_level and not inventory.inventory_requested:
                        inventory.inventory_requested = True
                        print(f'Placing request for {inventory.name}')
                        self.reorder_needed.append(inventory)
                        self.build_order()
                if self.stop:
                    break
        

        def lower_inventories(self):
            while True:
                for product, inventory in self.inventories.items():
                    inventory.lower_inventory(INVENTORY_DECREASE_RATE)
                time.sleep(random.randint(1, 5))
                if self.stop:
                    break
            
        
        def build_order(self):
            # Priority queue logic
            """
            I'm thinking I could handle it like tics. For example 1 tic the product can only wait max 1 second before having to be placed
            in an order. And for 3 it can wait max 3 seconds. And so on.
            So if a product runs out of tics it will be placed in the order. 
            """
            
        
        def place_request(self):
            print("Sending order to tms")

        def refill_inventory(self):
            print("Refilling inventory")

        def manage_docks(self):
        


    class DriverController:
        def create_driver(self)
            
        def finish_threads(self)



class Inventory:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.priority = random.randint(1,3)
        self.lock = threading.Lock()
        self.reorder_level = REORDER_LEVEL
        self.max_inventory = MAX_INVENTORY
        self.inventory_requested = False
    
    def lower_inventory(self, amount):
        with self.lock:
            self.quantity -= amount
            print(f'{amount} {self.name} removed from inventory')
    
    def increase_inventory(self, amount):
        with self.lock:
            self.quantity += amount
            print(f'{amount} {self.name} added to inventory')
    


inventories = dict()
for i in range(PRODUCT_TYPES):
    inventories[i] = Inventory(f'Product {i}', random.randint(30, MAX_INVENTORY))




class Bus:
    def __init__(self, name, available_seats):
        self.name = name
        self.lock = threading.Lock()
        self.available_seats = available_seats
    
    def book(self, seats):
        print(f"There are {self.available_seats} seats available for {self.name}")
        with self.lock:
            print(f'Booking {seats} seats for {self.name}')
            time.sleep(1)
            if self.available_seats < seats:
                print(f'Not enough seats available for {self.name}')
                return False
            self.available_seats -= seats
            print(f'{seats} seats booked for {self.name}')
            print(f'{self.available_seats} seats left for {self.name}')
            return True
        

class Costumer:
    def __init__(self, name, bus):
        self.name = name
        self.needed_seats = random.randint(1, 3)
        self.booking = self.book(bus, self.needed_seats)
    
    def book(self, bus, seats):
        time.sleep(random.randint(1, 3))
        print(f'{self.name} is trying to book {seats} seats on {bus.name}')
        if bus.book(seats):
            print(f'{self.name} booked {seats} seats on {bus.name}')
        else:
            print(f"{self.name} couldn't book {seats} seats on {bus.name}")
        
bus = Bus('Bus 1', 5)

t1 = time.perf_counter()
for i in range(5):
    thread = threading.Thread(target=Costumer, args=(f'Costumer {i}', bus)).start()


# Wait for other threads to finish
for thread in threading.enumerate():
    if thread is not threading.current_thread():
        thread.join()


t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')
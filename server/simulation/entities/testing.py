import random
import threading
import time



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
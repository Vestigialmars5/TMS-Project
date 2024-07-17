import random
import string

# Generate license plate number
def generate_vehicle_plate():
    return ''.join(random.choices(string.ascii_uppercase, k=3)) + ''.join(random.choices(string.digits, k=3))
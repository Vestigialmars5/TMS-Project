from enum import Enum
from typing import Dict, Type
MIN_NAME = 2
MAX_NAME = 30
MIN_PASSWORD = 8


class RoleType(Enum):
    ADMIN = (1, "Admin")
    TRANSPORTATION_MANAGER = (2, "Transportation Manager")
    CARRIER = (3, "Carrier")
    CUSTOMER = (4, "Customer")
    DRIVER = (5, "Driver")
    ACCOUNTING = (6, "Accounting")
    WAREHOUSE_MANAGER = (7, "Warehouse Manager")
    DISPATCHER = (8, "Dispatcher")
    CSR = (9, "Customer Service Representative")

    def __init__(self, id: int, display_name: str):
        self.id = id
        self.display_name = display_name

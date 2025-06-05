from lost_and_found.item import Item
from lost_and_found.enums import Category, ItemType
from .item import Item

class ElectronicItem(Item):
    def __init__(self, name, description, item_type, location, contact_info, brand, model, serial_number):
        super().__init__(name, description, item_type, location, contact_info)
        self.brand = brand
        self.model = model
        self.serial_number = serial_number


    def __str__(self):
        base = super().__str__()
        return (f"{base}\nElectronic Details - Brand: {self.brand}, "
                f"Model: {self.model}, Serial: {self.serial_number}")

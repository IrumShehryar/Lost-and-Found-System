from lost_and_found.item import Item
from lost_and_found.enums import Category, ItemType

class ElectronicItem(Item):
    def __init__(self, name, description, item_type, location, contact_info, brand, model, serial_number):
        # Initialize base item class
        super().__init__(name, description, item_type, Category.ELECTRONIC, location, contact_info)

        # Additional attributes specific to electronic items
        self.brand = brand                # Brand of the electronic item
        self.model = model                # Model identifier
        self.serial_number = serial_number  # Unique serial number of the item
from lost_and_found.item import Item
from lost_and_found.enums import Category, ItemType
from .item import Item

class NonElectronicItem(Item):
    def __init__(self, name, description, item_type, location, contact_info, material, color):
        super().__init__(name, description, item_type, location, contact_info)
        self.material = material
        self.color = color


    def __str__(self):
        base = super().__str__()
        return (f"{base}\nNon-Electronic Details - Material: {self.material}, "
                f"Color: {self.color}")

from lost_and_found.item import Item
from lost_and_found.enums import Category, ItemType

class NonElectronicItem(Item):
    def __init__(self, name, description, item_type, location, contact_info, material, color):
        # Initialize base items class
        super().__init__(name, description, item_type, Category.NON_ELECTRONIC, location, contact_info)

        # Additional attributes for non-electronic items
        self.material = material      # What material it's made of (e.g., fabric, plastic)
        self.color = color            # Color of the item

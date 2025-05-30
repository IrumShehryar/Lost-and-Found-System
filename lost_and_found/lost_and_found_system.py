
from lost_and_found.enums import ItemType
from lost_and_found.item import Item

class LostAndFoundSystem:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        """
        Add a new lost or found item to the system.
        """
        self.items.append(item)

    def search(self, item_type: ItemType, location: str) -> list[Item]:
        """
        Search for items by type and location.
        """
        matching_items = []
        for item in self.items:
            if item.item_type == item_type and location.lower() in item.location.lower():
                matching_items.append(item)
        return matching_items

    def display_items(self):
        """
        Print all items in the system (basic display function).
        """
        for item in self.items:
            print(item)
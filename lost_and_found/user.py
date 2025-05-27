from lost_and_found.weather import Weather
from lost_and_found.item import Item
from lost_and_found.enums import ItemType

class User:
    _id_counter = 1

    def __init__(self, name: str, email: str, phone: str, role: str):
        # Unique user ID
        self.user_id = User._id_counter
        User._id_counter += 1

        # User details
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role  # e.g., "Student" or "Staff"

    def report_item(self, system, item: Item):

        """
        User reports an item to the LostAndFoundSystem.
        """
        if item.item_type == ItemType.FOUND:
            item.weather_info = Weather.get_current_weather(item.location)
        system.add_item(item)

    def search_item(self, system, item_type: ItemType, location: str) -> list[Item]:
        """
        Search for items in the system based on type and location.
        """
        return system.search(item_type, location)

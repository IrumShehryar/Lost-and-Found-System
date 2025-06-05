from lost_and_found.enums import Category, Status, ItemType

class Item:
    _id_counter = 1  # class-level counter

    def __init__(self, name, description, item_type, location, contact_info):
        self.item_id = Item._id_counter
        Item._id_counter += 1

        self.name = name
        self.description = description
        self.item_type = item_type
        self.location = location
        self.contact_info = contact_info
        self.status = Status.UNRESOLVED
        self.weather_info = None  # default


    def update_status(self, new_status):
        """
        Update the status of the item.
        """
        self.status = new_status               #what is this??????

    def matches(self, other_item):
        return (
                self.name.lower() == other_item.name.lower() and
                self.category == other_item.category and
                self.location.lower() == other_item.location.lower()
        )

    def __str__(self):
        return (f"[{self.item_id}] {self.name} ({self.item_type.value}) - "
                f"{self.category.value} - {self.description} at {self.location} "
                f"Status: {self.status.value}")


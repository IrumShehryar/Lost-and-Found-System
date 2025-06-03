from lost_and_found.enums import Category, Status, ItemType

class Item:
    # Class-level counter to assign unique item IDs
    _id_counter = 1

    def __init__(self, name, description, item_type, category, location, contact_info):
        # Unique identifier for the item
        self.item_id = Item._id_counter
        Item._id_counter += 1

        # Basic item attributes
        self.name = name                      # Name of the item
        self.description = description        # Description of the item
        self.item_type = item_type            # Enum: LOST or FOUND
        self.category = category              # Enum: ELECTRONIC or NON_ELECTRONIC
        self.location = location              # Where it was lost/found
        self.contact_info = contact_info      # Contact of the person reporting

        # Status of the item, default is unresolved
        self.status = Status.UNRESOLVED

        # Weather info to be fetched when needed
        self.weather_info = None

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


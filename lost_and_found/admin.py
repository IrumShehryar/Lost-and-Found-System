from lost_and_found.user import User
from lost_and_found.enums import Status, ItemType
from lost_and_found.item import Item

class Admin(User):
    def __init__(self, name, email, phone, role="Admin"):
        # Admin is also a User, with role preset to "Admin"
        super().__init__(name, email, phone, role)

    def match_items(self, lost_item, found_item):
        return (
                lost_item.name.strip().lower() == found_item.name.strip().lower()
                and lost_item.item_type == ItemType.LOST
                and found_item.item_type == ItemType.FOUND
                and lost_item.status == Status.UNRESOLVED
                and found_item.status == Status.UNRESOLVED
        )

    def resolve_items(self,lost_item: Item, found_item: Item):
        #Update the status of both items to RESOLVED
        lost_item.update_status(Status.RESOLVED)
        found_item.update_status(Status.RESOLVED)

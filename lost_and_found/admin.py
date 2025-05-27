from lost_and_found.user import User
from lost_and_found.enums import Status
from lost_and_found.item import Item

class Admin(User):
    def __init__(self, name, email, phone, role="Admin"):
        # Admin is also a User, with role preset to "Admin"
        super().__init__(name, email, phone, role)

    def match_items(self, lost_item: Item, found_item: Item)-> bool:
        # Use the item's match method to compare lost and found items
        return lost_item.matches(found_item)

    def resolve_items(self,lost_item: Item, found_item: Item):
        #Update the status of both items to RESOLVED
        lost_item.update_status(Status.RESOLVED)
        found_item.update_status(Status.RESOLVED)

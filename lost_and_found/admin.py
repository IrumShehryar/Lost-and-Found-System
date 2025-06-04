from lost_and_found.user import User
from lost_and_found.enums import Status
from lost_and_found.item import Item

class Admin(User):
    def __init__(self, name, email, phone, role="Admin"):
        # Admin is also a User, with role preset to "Admin"
        super().__init__(name, email, phone, role)

    def match_items(self, lost_item, found_item):
        return (
                lost_item.name.lower() == found_item.name.lower() and
                isinstance(lost_item, type(found_item)) and
                getattr(lost_item, "brand", "") == getattr(found_item, "brand", "") and
                getattr(lost_item, "model", "") == getattr(found_item, "model", "")
        )

    def resolve_items(self,lost_item: Item, found_item: Item):
        #Update the status of both items to RESOLVED
        lost_item.update_status(Status.RESOLVED)
        found_item.update_status(Status.RESOLVED)

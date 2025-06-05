from lost_and_found.user import User
from lost_and_found.enums import Status
from lost_and_found.item import Item


class Admin(User):
    """
    Represents an Admin user who can match and resolve lost and found items.
    """

    def __init__(self, name: str, email: str, phone: str, role: str = "Admin"):
        """
        Initialize an Admin with preset role.
        """
        super().__init__(name, email, phone, role)

    def match_items(self, lost_item: Item, found_item: Item) -> bool:
        """
        Determine if two items match using the item's match logic.

        :param lost_item: The lost item.
        :param found_item: The found item.
        :return: True if the items match, False otherwise.
        """
        return lost_item.matches(found_item)

    def resolve_items(self, lost_item: Item, found_item: Item) -> None:
        """
        Mark both items as resolved.

        :param lost_item: The lost item to resolve.
        :param found_item: The found item to resolve.
        """
        if not self.match_items(lost_item, found_item):
            raise ValueError("Items do not match and cannot be resolved.")

        lost_item.update_status(Status.RESOLVED)
        found_item.update_status(Status.RESOLVED)

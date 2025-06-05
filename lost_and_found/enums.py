
from enum import Enum

class ItemType(Enum):
    """Represents whether an item is lost or found."""
    LOST = "Lost"
    FOUND = "Found"

    def __str__(self):
        return self.value

class Category(Enum):
    """Represents the category of an item."""
    ELECTRONIC = "Electronic"
    NON_ELECTRONIC = "Non-Electronic"

    def __str__(self):
        return self.value

class Status(Enum):
    """Represents the resolution status of an item."""
    UNRESOLVED = "Unresolved"
    RESOLVED = "Resolved"

    def __str__(self):
        return self.value

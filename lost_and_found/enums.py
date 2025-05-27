from enum import Enum

class ItemType(Enum):
    LOST = "Lost"
    FOUND = "Found"

class Category(Enum):
    ELECTRONIC = "Electronic"
    NON_ELECTRONIC = "Non-Electronic"

class Status(Enum):
    UNRESOLVED = "Unresolved"
    RESOLVED = "Resolved"

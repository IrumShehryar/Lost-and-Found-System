import pytest

# Importing enumerations from the lost_and_found module
# These enums represent the types of items, their categories, and resolution status
from lost_and_found.enums import ItemType, Category, Status

# Test function to check the values of ItemType enumeration
def test_item_type_values():
    # Asserts that the value of the LOST enum member is "Lost"
    assert ItemType.LOST.value == "Lost"
    # Asserts that value of FOUND enum member is "Found"
    assert ItemType.FOUND.value == "Found"

# Test function to verify the values of Category enumeration
def test_category_values():
    # Asserts that the value of the ELECTRONIC enum member is "Electronic"
    assert Category.ELECTRONIC.value == "Electronic"
    # Asserts that the value of the NON_ELECTRONIC enum member is "Non-Electronic"
    assert Category.NON_ELECTRONIC.value == "Non-Electronic"

# Test function to check values of Status enumeration
def test_status_values():
    # Asserts that the value of the UNRESOLVED enum member is "Unresolved"
    assert Status.UNRESOLVED.value == "Unresolved"
    # Asserts that the value of the RESOLVED enum member is "Resolved"
    assert Status.RESOLVED.value == "Resolved"

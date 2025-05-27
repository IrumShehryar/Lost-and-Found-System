import pytest
from lost_and_found.enums import ItemType , Category, Status

def test_item_type_values():
   assert ItemType.LOST.value == "Lost"
   assert ItemType.FOUND.value == "Found"

def test_category_values():
    assert Category.ELECTRONIC.value == "Electronic"
    assert Category.NON_ELECTRONIC.value == "Non-Electronic"

def test_status_values():
    assert Status.UNRESOLVED.value == "Unresolved"
    assert Status.RESOLVED.value == "Resolved"
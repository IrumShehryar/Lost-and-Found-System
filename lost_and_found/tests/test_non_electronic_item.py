import pytest
from lost_and_found.enums import ItemType
from lost_and_found.non_electronic_item import NonElectronicItem

def test_non_electronic_item_fields():
    item = NonElectronicItem("Bottle", "Water bottle", ItemType.FOUND, "Cafeteria", "87654123", "Steel", "Silver")
    assert item.material == "Steel"
    assert item.color == "Silver"

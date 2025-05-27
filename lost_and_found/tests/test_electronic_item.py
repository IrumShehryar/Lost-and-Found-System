import pytest
from lost_and_found.enums import ItemType
from lost_and_found.electronic_item import ElectronicItem

def test_electronic_item_fields():
    item = ElectronicItem("Laptop", "Gaming laptop", ItemType.LOST, "Library", "76876553", "HP", "Envy", "SN001")
    assert item.brand == "HP"
    assert item.model == "Envy"
    assert item.serial_number == "SN001"

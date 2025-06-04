import pytest
from lost_and_found.enums import ItemType
from lost_and_found.electronic_item import ElectronicItem
# Define a test function to verify the behavior of the ElectronicItem class
def test_electronic_item_fields():
    # Create an ElectronicItem with full details including brand, model, and serial number
    item = ElectronicItem("Laptop", "Gaming laptop", ItemType.LOST, "Library", "76876553", "HP", "Envy", "SN001")
    # Validate that the object's fields were correctly assigned
    assert item.brand == "HP"
    assert item.model == "Envy"
    assert item.serial_number == "SN001"

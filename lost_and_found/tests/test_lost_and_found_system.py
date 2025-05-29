import pytest
from lost_and_found.enums import ItemType, Category
from lost_and_found.item import Item
from lost_and_found.lost_and_found_system import LostAndFoundSystem


# Test case to check if an item can be successfully added to the LostAndFoundSystem
def test_add_item():
    # Create a new instance of the LostAndFoundSystem
    system = LostAndFoundSystem()

    # Create an item of type LOST and category ELECTRONIC
    item = Item("Phone", "Black phone", ItemType.LOST, Category.ELECTRONIC, "Library", "65438765")

    # Add the item to the system
    system.add_item(item)

    # Verify that the item is now present in the system's list of items
    assert item in system.items


# Test case to check if searching for items based on type and location works correctly
def test_search_items():
    # Create a new instance of the LostAndFoundSystem
    system = LostAndFoundSystem()

    # Create an item of type FOUND and category NON_ELECTRONIC
    item = Item("Keys", "Set of keys", ItemType.FOUND, Category.NON_ELECTRONIC, "Gate", "67456372")

    # Add the item to the system
    system.add_item(item)

    # Search for items that are of type FOUND and located at "Gate"
    results = system.search(ItemType.FOUND, "Gate")

    # Verify that exactly one item is returned
    assert len(results) == 1

    # Verify that the returned item's name is "Keys"
    assert results[0].name == "Keys"


# Test case to ensure that added items are retained in the internal list of items
def test_display_items_returns_list():
    # Create a new instance of the LostAndFoundSystem
    system = LostAndFoundSystem()

    # Create an item of type LOST and category NON_ELECTRONIC
    item = Item("Notebook", "Blue notebook", ItemType.LOST, Category.NON_ELECTRONIC, "Classroom", "44876521")

    # Add the item to the system
    system.add_item(item)

    # Check if an item with the name "Notebook" exists in the system's item list
    found = False
    for i in system.items:
        if i.name == "Notebook":
            found = True
            break

    # Assert that the item was found in the list
    assert found

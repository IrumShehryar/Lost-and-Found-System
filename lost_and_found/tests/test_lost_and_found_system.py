import pytest
from lost_and_found.enums import ItemType, Category
from lost_and_found.item import Item
from lost_and_found.lost_and_found_system import LostAndFoundSystem

def test_add_item():
    system = LostAndFoundSystem()
    item = Item("Phone", "Black phone", ItemType.LOST, Category.ELECTRONIC, "Library", "65438765")
    system.add_item(item)
    assert item in system.items

def test_search_items():
    system = LostAndFoundSystem()
    item = Item("Keys", "Set of keys", ItemType.FOUND, Category.NON_ELECTRONIC, "Gate", "67456372")
    system.add_item(item)
    results = system.search(ItemType.FOUND, "Gate")
    assert len(results) == 1
    assert results[0].name == "Keys"

def test_display_items_returns_list():
    system = LostAndFoundSystem()
    item = Item("Notebook", "Blue notebook", ItemType.LOST, Category.NON_ELECTRONIC, "Classroom", "44876521")
    system.add_item(item)

    # To check if "Notebook" is present
    found = False
    for i in system.items:
        if i.name == "Notebook":
            found = True
            break
    assert found
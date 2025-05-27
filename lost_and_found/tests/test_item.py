import pytest
from lost_and_found.enums import ItemType, Category, Status
from lost_and_found.item import Item

def test_item_creation():
    item = Item("Phone","Black Iphone", ItemType.LOST, Category.ELECTRONIC, "Library", "44123462")
    assert item.name == "Phone"
    assert item.status == Status.UNRESOLVED
    assert isinstance(item.item_id , int)

def test_update_status():
    item =  Item("Wallet", "Leather wallet", ItemType.LOST, Category.NON_ELECTRONIC, "Cafeteria", "56542315")
    item.update_status(Status.RESOLVED)
    assert item.status == Status.RESOLVED

def test_item_matches():
    item1 = Item("Bag", "Blue backpack", ItemType.LOST, Category.NON_ELECTRONIC, "Main Gate", "34527653")
    item2 = Item("Bag", "Blue backpack", ItemType.FOUND, Category.NON_ELECTRONIC, "Main Gate", "76547654")
    assert item1.matches(item2)

def test_unique_item_ids():
    item1 = Item("Book", "Math textbook", ItemType.LOST, Category.NON_ELECTRONIC, "Classroom", "78765622")
    item2 = Item("Pen", "Blue ink pen", ItemType.FOUND, Category.NON_ELECTRONIC, "Library", "98765472")
    assert item1.item_id != item2.item_id
import pytest
from lost_and_found.enums import Category, ItemType
from lost_and_found.item import Item
from lost_and_found.user import User
from lost_and_found.lost_and_found_system import LostAndFoundSystem

# Test: user reports a found item
def test_user_can_report_item_to_system():
    user = User("Iqra", "iqra@gmail.com", "123456789", "Student")
    system = LostAndFoundSystem()
    item = Item("Watch", "Smartwatch", ItemType.FOUND, Category.ELECTRONIC, "Helsinki", "123456789")
    user.report_item(system, item)
    assert item in system.items
    # assert item.weather_info == "Weather not implemented"  # Placeholder for future

# Test: user searches for lost item
def test_user_can_search_items_in_system():
    user = User("Iqra", "iqra@gmail.com", "123456789", "Student")
    system = LostAndFoundSystem()
    item1 = Item("Notebook", "Blue notebook", ItemType.LOST, Category.NON_ELECTRONIC, "Library", "44365432")
    item2 = Item("Charger", "Phone charger", ItemType.FOUND, Category.ELECTRONIC, "Lab", "99876446")
    system.add_item(item1)
    system.add_item(item2)
    results = user.search_item(system, ItemType.LOST, "Library")
    assert len(results) == 1
    assert results[0].name == "Notebook"

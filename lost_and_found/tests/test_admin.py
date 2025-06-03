import pytest
from lost_and_found.enums import ItemType, Category, Status
from lost_and_found.item import Item
from lost_and_found.admin import Admin

def test_match_items():
    admin = Admin("Admin User", "irum@gmail.com", "449328224")
    # Create a lost item and a found item with matching attributes
    lost = Item("Phone", "Black iPhone", ItemType.LOST, Category.ELECTRONIC, "Library", "75643212")
    found = Item("Phone", "Black iPhone", ItemType.FOUND, Category.ELECTRONIC, "Library", "75643212")

    # Assert that the admin is able to match the two items based on similarity
    assert admin.match_items(lost, found) is True

def test_resolve_items():
    admin = Admin("Admin User", "irum@gmail.com", "449328224")
    lost = Item("Wallet", "Leather wallet", ItemType.LOST, Category.NON_ELECTRONIC, "Gate", "64744333")
    found = Item("Wallet", "Leather wallet", ItemType.FOUND, Category.NON_ELECTRONIC, "Gate", "72727822")
    admin.resolve_items(lost, found)
    assert lost.status == Status.RESOLVED
    assert found.status == Status.RESOLVED
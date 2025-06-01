from lost_and_found.enums import ItemType, Category
from lost_and_found.item import Item
from lost_and_found.lost_and_found_system import LostAndFoundSystem
from lost_and_found.user import User
from lost_and_found.admin import Admin

def main():
    system = LostAndFoundSystem()
    user = User("Iqra", "iqra@example.com", "123456789", "Student")
    admin = Admin("Admin", "admin@example.com", "000000000")

    # User reports a found item
    found_item = Item("Phone", "Black iPhone", ItemType.FOUND, Category.ELECTRONIC, "Library", "iqra@example.com")
    user.report_item(system, found_item)

    # Another item reported as lost
    lost_item = Item("Phone", "Black iPhone", ItemType.LOST, Category.ELECTRONIC, "Library", "xyz@example.com")
    user.report_item(system, lost_item)

    # Admin matches and resolves them
    if admin.match_items(lost_item, found_item):
        admin.resolve_items(lost_item, found_item)
        print("Items matched and resolved.")

    # ✅ USE __str__ method for full formatted output
    for item in system.items:
        print(item)

if __name__ == "__main__":
    main()

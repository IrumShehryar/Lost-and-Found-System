from lost_and_found.enums import ItemType, Category,Status
from lost_and_found.item import Item
from lost_and_found.lost_and_found_system import LostAndFoundSystem
from lost_and_found.user import User
from lost_and_found.admin import Admin
from lost_and_found.electronic_item import ElectronicItem
from lost_and_found.non_electronic_item import NonElectronicItem
from lost_and_found.weather import Weather


import os
import time


# ---------- HELPER FUNCTIONS ----------

def clear_screen():
    """Clear the terminal screen based on the OS."""
    os.system("cls" if os.name == "nt" else "clear")

# halt for some time
def pause():
    """Pause the screen until the user presses Enter."""
    input("\nPress Enter to continue...")


def print_header(title):
    """Print a formatted title for each section."""
    print("=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)


def extract_city(location: str) -> str:
    """
    Extracts the likely city from a location string.
    Assumes the last comma-separated value is the city.
    Example: 'Library, Helsinki' → 'Helsinki'
    """
    parts = location.split(",")
    return parts[-1].strip() if len(parts) > 1 else location.strip()


# ---------- USER & STAFF WORKFLOW ----------

def report_flow(user, system):
    """Allow a student or staff member to report a lost or found item."""
    clear_screen()
    print_header("Report Item")

    # Ask for basic classification
    item_type = ItemType[input("Enter item type (LOST/FOUND): ").strip().upper()]
    category = Category[input("Enter item category (ELECTRONIC/NON_ELECTRONIC): ").strip().upper()]

    # Collect common info
    name = input("Item name: ")
    description = input("Description: ")
    location = input("Location (e.g., 'Library, Helsinki'): ")
    contact_info = input("Your contact info: ")

    # Gather category-specific fields
    if category == Category.ELECTRONIC:
        brand = input("Brand: ")
        model = input("Model: ")
        serial = input("Serial number: ")
        item = ElectronicItem(name, description, item_type, location, contact_info, brand, model, serial)
    else:
        material = input("Material: ")
        color = input("Color: ")
        item = NonElectronicItem(name, description, item_type, location, contact_info, material, color)

    # Attach weather info if the item is FOUND
    if item_type == ItemType.FOUND:
        city = extract_city(location)
        item.weather_info = Weather.get_current_weather(city)

    # Submit the item to the system
    user.report_item(system, item)
    print("\n✅ Item reported successfully!")
    pause()


def search_flow(user, system):
    """Allow user to search for lost or found items."""
    clear_screen()
    print_header("Search Items")

    item_type = ItemType[input("Search for (LOST/FOUND): ").strip().upper()]
    location = input("Enter location keyword (e.g., 'Espoo'): ")

    results = user.search_item(system, item_type, location)

    if results:
        print("\n🟢 Matching items found:")
        for item in results:
            print(f"\n{item}")
    else:
        print("\n⚠ No items matched your search.")
    pause()


# ---------- ADMIN WORKFLOW ----------

def admin_flow(admin, system):
    """Admin menu to view unresolved items and match & resolve them."""
    while True:
        clear_screen()
        print_header("Admin Panel")
        print("1. View Unresolved Items")
        print("2. Match & Resolve Items")
        print("3. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            # Show only unresolved items
            print_header("Unresolved Items")
            unresolved_items = [item for item in system.get_all_items() if item.status == Status.UNRESOLVED]

            if unresolved_items:
                for item in unresolved_items:
                    print(f"\n{item}")
            else:
                print("\n✅ All items have been resolved!")
            pause()

        elif choice == "2":
            # Match and resolve a pair of items
            try:
                lid = int(input("Enter Lost Item ID: "))
                fid = int(input("Enter Found Item ID: "))

                lost = next((i for i in system.items if i.item_id == lid and i.item_type == ItemType.LOST), None)
                found = next((i for i in system.items if i.item_id == fid and i.item_type == ItemType.FOUND), None)

                if lost and found:
                    if admin.match_items(lost, found):
                        admin.resolve_items(lost, found)
                        print("\n✅ Items matched and resolved.")
                    else:
                        print("\n❌ Items do not match.")
                else:
                    print("\n⚠ One or both IDs not found.")
            except ValueError:
                print("\n❌ Please enter numeric IDs only.")
            pause()

        elif choice == "3":
            break  # Exit to main menu
        else:
            print("Invalid choice.")
            time.sleep(1)


# ---------- MAIN FUNCTION ----------

def main():
    """Entry point: handles user type selection and role-specific flows."""
    system = LostAndFoundSystem()

    while True:
        clear_screen()
        print_header("Lost and Found System")
        print("1. Login as Student or Staff")
        print("2. Login as Admin")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            # STUDENT or STAFF
            name = input("Your name: ")
            email = input("Your email: ")
            phone = input("Your phone: ")
            role_input = input("Are you a Student or Staff? (student/staff): ").strip().lower()
            role = "Staff" if role_input == "staff" else "Student"

            user = User(name, email, phone, role)

            while True:
                clear_screen()
                print_header(f"{role} Menu")
                print("1. Report Item")
                print("2. Search Items")
                print("3. Logout")

                opt = input("Choose an option: ")

                if opt == "1":
                    report_flow(user, system)
                elif opt == "2":
                    search_flow(user, system)
                elif opt == "3":
                    break  # Go back to main menu
                else:
                    print("Invalid choice.")
                    time.sleep(1)

        elif choice == "2":
            # ADMIN
            name = input("Admin name: ")
            email = input("Admin email: ")
            phone = input("Admin phone: ")

            admin = Admin(name, email, phone)
            admin_flow(admin, system)

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice.")
            time.sleep(1)


# ---------- EXECUTION START ----------
if __name__ == "__main__":
    main()



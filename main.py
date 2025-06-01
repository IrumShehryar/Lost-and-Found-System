import os
import time
from rich.console import Console
from rich.table import Table
from rich import box

from lost_and_found.enums import ItemType, Category, Status
from lost_and_found.item import Item
from lost_and_found.lost_and_found_system import LostAndFoundSystem
from lost_and_found.user import User
from lost_and_found.admin import Admin
from lost_and_found.electronic_item import ElectronicItem
from lost_and_found.non_electronic_item import NonElectronicItem
from lost_and_found.weather import Weather

console = Console()


# ---------- HELPER FUNCTIONS ----------
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def wait():
    input("\nPress Enter to continue...")


def title(text):
    console.rule(f"[bold blue]{text}", style="bright_magenta")


def get_city(location):
    return location.split(",")[-1].strip() if "," in location else location.strip()


# ---------- USER FUNCTIONS ----------
def report_item(user, system):
    clear()
    title("Report Lost or Found Item")

    try:
        item_type = ItemType[input("Item Type (LOST/FOUND): ").strip().upper()]
        category = Category[input("Category (ELECTRONIC/NON_ELECTRONIC): ").strip().upper()]
    except KeyError:
        console.print("[red]Invalid input.[/red]")
        wait()
        return

    name = input("Item Name: ")
    desc = input("Description: ")
    location = input("Location (e.g., Library, Espoo): ")
    contact = input("Your Contact Info: ")

    if category == Category.ELECTRONIC:
        brand = input("Brand: ")
        model = input("Model: ")
        serial = input("Serial Number: ")
        item = ElectronicItem(name, desc, item_type, location, contact, brand, model, serial)
    else:
        material = input("Material: ")
        color = input("Color: ")
        item = NonElectronicItem(name, desc, item_type, location, contact, material, color)

    if item_type == ItemType.FOUND:
        item.weather_info = Weather.get_current_weather(get_city(location))

    user.report_item(system, item)
    console.print("\n[green]✅ Item reported![/green]")
    wait()


def search_items(user, system):
    clear()
    title("Search Items")

    try:
        item_type = ItemType[input("Looking for (LOST/FOUND): ").strip().upper()]
    except KeyError:
        console.print("[red]Invalid item type.[/red]")
        wait()
        return

    keyword = input("Location keyword: ")
    results = user.search_item(system, item_type, keyword)

    if results:
        table = Table(title="Matching Items", box=box.SIMPLE, header_style="bold blue")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Type")
        table.add_column("Location")
        table.add_column("Status")

        for item in results:
            table.add_row(str(item.item_id), item.name, item.item_type.value, item.location, item.status.value)

        console.print(table)
    else:
        console.print("\n[yellow]No matching items found.[/yellow]")
    wait()


# ---------- ADMIN FUNCTIONS ----------
def admin_menu(admin, system):
    while True:
        clear()
        title("Admin Menu")
        print("1. View Unresolved Items")
        print("2. Match Items")
        print("3. Logout")

        opt = input("Choose: ")
        if opt == "1":
            clear()
            title("Unresolved Items")
            items = [i for i in system.get_all_items() if i.status == Status.UNRESOLVED]
            if items:
                for i in items:
                    console.print(i)
            else:
                console.print("[green]No unresolved items.[/green]")
            wait()
        elif opt == "2":
            try:
                lid = int(input("Lost Item ID: "))
                fid = int(input("Found Item ID: "))

                lost = next((i for i in system.items if i.item_id == lid and i.item_type == ItemType.LOST), None)
                found = next((i for i in system.items if i.item_id == fid and i.item_type == ItemType.FOUND), None)

                if lost and found and admin.match_items(lost, found):
                    admin.resolve_items(lost, found)
                    console.print("\n[green]✅ Match successful![/green]")
                else:
                    console.print("\n[red]❌ Match failed or invalid IDs.[/red]")
            except ValueError:
                console.print("[red]Enter valid numbers.[/red]")
            wait()
        elif opt == "3":
            break
        else:
            console.print("[red]Invalid option.[/red]")
            time.sleep(1)


# ---------- MAIN FUNCTION ----------
def main():
    system = LostAndFoundSystem()

    while True:
        clear()
        title("Lost and Found System")
        print("1. Login as Student/Staff")
        print("2. Login as Admin")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Your Name: ")
            email = input("Your Email: ")
            phone = input("Your Phone: ")
            role = input("Student or Staff: ").strip().capitalize()
            user = User(name, email, phone, role)

            while True:
                clear()
                title(f"{role} Menu")
                print("1. Report an Item")
                print("2. Search Items")
                print("3. Logout")

                op = input("Choose: ")
                if op == "1":
                    report_item(user, system)
                elif op == "2":
                    search_items(user, system)
                elif op == "3":
                    break
                else:
                    console.print("[red]Invalid option.[/red]")
                    time.sleep(1)

        elif choice == "2":
            name = input("Admin Name: ")
            email = input("Admin Email: ")
            phone = input("Admin Phone: ")
            admin = Admin(name, email, phone)
            admin_menu(admin, system)

        elif choice == "3":
            console.print("[bold green]Goodbye![/bold green]")
            break

        else:
            console.print("[red]Invalid choice.[/red]")
            time.sleep(1)


# ---------- START PROGRAM ----------
if __name__ == "__main__":
    main()
import os
import time
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
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
    console.print("\n[grey62]Press Enter to continue...[/grey62]")
    input()

def title(text):
    panel = Panel(
        Text(text, justify="center", style="bold magenta"),
        style="bright_blue",
        expand=True,
        padding=(0, 2),
    )
    console.print(panel)

def get_city(location):
    return location.split(",")[-1].strip() if "," in location else location.strip()

def is_valid_email(email):
    return "@" in email and "." in email and re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


# ---------- USER FUNCTIONS ----------
def report_item(user, system):
    clear()
    title("Report Lost or Found Item")

    try:
        item_type = ItemType[console.input("[bold blue]Item Type (LOST/FOUND): [/bold blue]").strip().upper()]
        category = Category[console.input("[bold blue]Category (ELECTRONIC/NON_ELECTRONIC): [/bold blue]").strip().upper()]
    except KeyError:
        console.print("[bold red]❌ Invalid input. Please enter correct item type and category.[/bold red]")
        wait()
        return

    name = console.input("[bold yellow]Item Name:[/] ")
    desc = console.input("[bold yellow]Description:[/] ")
    location = console.input("[bold yellow]Location (e.g., Library, Espoo):[/] ")
    contact = console.input("[bold yellow]Your Contact Info:[/] ")

    if category == Category.ELECTRONIC:
        brand = console.input("[bold yellow]Brand:[/] ")
        model = console.input("[bold yellow]Model:[/] ")
        serial = console.input("[bold yellow]Serial Number:[/] ")
        item = ElectronicItem(name, desc, item_type, location, contact, brand, model, serial)
    else:
        material = console.input("[bold yellow]Material:[/] ")
        color = console.input("[bold yellow]Color:[/] ")
        item = NonElectronicItem(name, desc, item_type, location, contact, material, color)

    if item_type == ItemType.FOUND:
        with console.status("[bold green]Fetching weather info...[/bold green]", spinner="earth"):
            item.weather_info = Weather.get_current_weather(get_city(location))

    user.report_item(system, item)
    console.print("\n[bold green]✅ Item reported successfully![/bold green]")

    if item.item_type == ItemType.FOUND and item.weather_info:
        console.print(f"[bold blue]🌦️ Weather at {item.location}: {item.weather_info}[/bold blue]")

    wait()


def search_items(user, system):
    clear()
    title("Search Items")

    try:
        item_type = ItemType[console.input("[bold blue]Looking for (LOST/FOUND): [/bold blue]").strip().upper()]
    except KeyError:
        console.print("[bold red]❌ Invalid item type entered.[/bold red]")
        wait()
        return

    keyword = console.input("[bold yellow]Location keyword:[/] ")
    results = user.search_item(system, item_type, keyword)

    if results:
        table = Table(
            title="Matching Items",
            box=box.ROUNDED,
            header_style="bold magenta",
            row_styles=["none", "dim"],
            show_lines=True,
        )
        table.add_column("ID", style="cyan", justify="center")
        table.add_column("Name", style="bold yellow")
        table.add_column("Type", style="green")
        table.add_column("Location", style="blue")
        table.add_column("Status", style="red")

        for item in results:
            table.add_row(str(item.item_id), item.name, item.item_type.value, item.location, item.status.value)

        console.print(table)
    else:
        console.print("\n[bold yellow]⚠️ No matching items found.[/bold yellow]")
    wait()


# ---------- ADMIN FUNCTIONS ----------
def admin_menu(admin, system):
    while True:
        clear()
        title("Admin Menu")

        panel = Panel.fit(
            "\n".join([
                "[bold cyan]1.[/] View Unresolved Items",
                "[bold cyan]2.[/] Match Items by Name",
                "[bold cyan]3.[/] Logout"
            ]),
            title="Select Option",
            border_style="bright_magenta"
        )
        console.print(panel)

        opt = console.input("[bold blue]Choose: [/bold blue]")

        if opt == "1":
            clear()
            title("Unresolved Items")
            items = [i for i in system.items if i.status == Status.UNRESOLVED]
            if items:
                for i in items:
                    console.print(f"[bold yellow]ID:[/] {i.item_id}  [bold yellow]Name:[/] {i.name}  [bold yellow]Type:[/] {i.item_type.value}  [bold yellow]Location:[/] {i.location}  [bold yellow]Status:[/] {i.status.value}")
            else:
                console.print("[bold green]✅ No unresolved items.[/bold green]")
            wait()

        elif opt == "2":
            clear()
            title("Match Lost and Found Items by Name")

            try:
                lost_name = console.input("[bold yellow]Lost Item Name:[/] ").strip().lower()
                found_name = console.input("[bold yellow]Found Item Name:[/] ").strip().lower()

                lost = next((i for i in system.items if i.name.lower() == lost_name and i.item_type == ItemType.LOST), None)
                found = next((i for i in system.items if i.name.lower() == found_name and i.item_type == ItemType.FOUND), None)

                if lost and found and admin.match_items(lost, found):
                    admin.resolve_items(lost, found)
                    console.print("\n[bold green]✅ Match successful! Items resolved.[/bold green]")
                else:
                    console.print("\n[bold red]❌ Match failed. Check item names and types.[/bold red]")
            except Exception as e:
                console.print(f"[bold red]An error occurred: {e}[/bold red]")
            wait()

        elif opt == "3":
            break

        else:
            console.print("[bold red]❌ Invalid option selected.[/bold red]")
            time.sleep(1)


# ---------- MAIN FUNCTION ----------
def main():
    system = LostAndFoundSystem()

    while True:
        clear()
        title("Lost and Found System")

        panel = Panel.fit(
            "\n".join([
                "[bold cyan]1.[/] Login as Student/Staff",
                "[bold cyan]2.[/] Login as Admin",
                "[bold cyan]3.[/] Exit"
            ]),
            title="Main Menu",
            border_style="bright_magenta"
        )
        console.print(panel)

        choice = console.input("[bold blue]Choose: [/bold blue]")

        if choice == "1":
            name = console.input("[bold yellow]Your Name:[/] ")

            while True:
                email = console.input("[bold yellow]Your Email:[/] ")
                if is_valid_email(email):
                    break
                else:
                    console.print("[bold red]❌ Invalid email. Please enter a valid email (e.g., abc@example.com).[/bold red]")

            while True:
                phone = console.input("[bold yellow]Your Phone (10 digits):[/] ")
                if is_valid_phone(phone):
                    break
                else:
                    console.print("[bold red]❌ Invalid phone number. It must be exactly 10 digits.[/bold red]")

            role = console.input("[bold yellow]Student or Staff:[/] ").strip().capitalize()
            user = User(name, email, phone, role)

            while True:
                clear()
                title(f"{role} Menu")

                panel = Panel.fit(
                    "\n".join([
                        "[bold cyan]1.[/] Report an Item",
                        "[bold cyan]2.[/] Search Items",
                        "[bold cyan]3.[/] Logout"
                    ]),
                    title=f"{role} Options",
                    border_style="bright_magenta"
                )
                console.print(panel)

                op = console.input("[bold blue]Choose: [/bold blue]")

                if op == "1":
                    report_item(user, system)
                elif op == "2":
                    search_items(user, system)
                elif op == "3":
                    break
                else:
                    console.print("[bold red]❌ Invalid option.[/bold red]")
                    time.sleep(1)

        elif choice == "2":
            name = console.input("[bold yellow]Admin Name:[/] ")

            while True:
                email = console.input("[bold yellow]Admin Email:[/] ")
                if is_valid_email(email):
                    break
                else:
                    console.print("[bold red]❌ Invalid email. Please enter a valid email (e.g., admin@example.com).[/bold red]")

            while True:
                phone = console.input("[bold yellow]Admin Phone (10 digits):[/] ")
                if is_valid_phone(phone):
                    break
                else:
                    console.print("[bold red]❌ Invalid phone number. It must be exactly 10 digits.[/bold red]")

            admin = Admin(name, email, phone)
            admin_menu(admin, system)

        elif choice == "3":
            console.print("[bold green]👋 Goodbye![/bold green]")
            break

        else:
            console.print("[bold red]❌ Invalid choice.[/bold red]")
            time.sleep(1)


# ---------- START PROGRAM ----------
if __name__ == "__main__":
    main()

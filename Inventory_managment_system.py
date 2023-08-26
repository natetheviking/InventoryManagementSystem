import sqlite3


class InventoryManagementSystem:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add_item(self, name, quantity, price):
        self.cursor.execute("INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
        self.conn.commit()

    def display_inventory(self):
        self.cursor.execute("SELECT * FROM items")
        items = self.cursor.fetchall()

        if not items:
            print("Inventory is empty.")
        else:
            for item in items:
                print(f"Item ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Price: {item[3]}")

    def close(self):
        self.conn.close()


def main():
    system = InventoryManagementSystem('inventory.db')

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            system.add_item(item_name, quantity, price)
            print("Item added to inventory.")
        elif choice == "2":
            system.display_inventory()
        elif choice == "3":
            system.close()
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

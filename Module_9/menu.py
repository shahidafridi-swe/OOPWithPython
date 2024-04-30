class Menu:
    def __init__(self) -> None:
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)
        print(f"{item.quantity}pc {item.name} added successfully!")

    def show_menu(self):
        print("------- Menu List -------")
        print("Nmae\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price} BDT\t{item.quantity}")

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"{item_name} item removed successfully!")
        else:
            print(f"{item} not found")
 
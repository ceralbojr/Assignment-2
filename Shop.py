class shop:

    # Attributes
    Name = ''
    Description = ''
    listOfCategories = ''
    listOfItems = ''
    URL = ''


    # Methods
    def viewCategory(self, category):
        print(f"Showing items in the {category} category:")
        for item in self.ListOfItems:
            if item.Category == category:
                print(f"{item.Title} ({item.Price})")

    def searchItems(self, keyword):
        print(f"Searching for items with keyword '{keyword}':")
        for item in self.ListOfItems:
            if keyword in item.Title or keyword in item.Description:
                print(f"{item.Title} ({item.Price})")

    def viewItems(self):
        print("Showing all items:")
        for item in self.ListOfItems:
            print(f"{item.Title} ({item.Price})")

    def viewShoppingCart(self, cart):
        total = 0
        print("Shopping cart contents:")
        for item in cart:
            print(f"{item.Title} ({item.Price})")
            total += item.Price
        print(f"Total cost: {total}")
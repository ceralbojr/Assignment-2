class shoppingCart:

    # Attributes
    listOfItems = ''
    DeliveryFess = 0
    Discount = 0
    TotalAmount = 0

    # Methods
    def addItem(self, item):
        self.ListOfItems.append(item)

    def removeItem(self, item):
        self.ListOfItems.remove(item)

    def selectDeliveryOption(self, delivery_option):
        if delivery_option == "Standard":
            self.DeliveryFees = 5
        elif delivery_option == "Express":
            self.DeliveryFees = 10
        else:
            print("Invalid delivery option selected.")

    def applyDiscount(self, discount):
        self.Discount = discount

    def calculateTotal(self):
        subtotal = 0
        for item in self.ListOfItems:
            subtotal += item.Price
        self.TotalAmount = subtotal + self.DeliveryFees - self.Discount

    def checkOut(self):
        print("Checking out...")
        self.calculateTotal()
        print(f"Total amount due: {self.TotalAmount}")
        # Payment processing code here

class order:

    # Attributes
    Date = ''
    Status = ''
    ShoppingCart = ''
    DeliveryAddress = ''
    PaymentMethod = ''

    # Methods
    def validatePayment(self):
        print("Validating payment...")
        # Payment validation code here
        self.Status = "Payment Validated"

    def cancel(self):
        print("Cancelling order...")
        self.Status = "Cancelled"

    def dispatch(self):
        print("Dispatching order...")
        self.Status = "Dispatched"

    def confirmDelivery(self):
        print("Confirming delivery...")
        self.Status = "Delivered"

    def refund(self):
        print("Refunding order...")
        # Refund processing code here
        self.Status = "Refunded"

    def archive(self):
        print("Archiving order...")
        # Archival code here
        self.Status = "Archived"
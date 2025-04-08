# Simple Smartphone class
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def call(self):
        print(f"Making a call using the {self.brand} {self.model}")
    
    def send_message(self, message):
        print(f"Sending message: {message}")

# Example usage:
my_phone = Smartphone("Apple", "iPhone 12")
my_phone.call()
my_phone.send_message("Hello there!")
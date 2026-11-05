from abc import ABC, abstractmethod


# 1. INHERITANCE (Generalization) - "Is-a"

print("--- 1. Inheritance ---")

class Animal:
    def __init__(self, name: str):
        self.name = name

class Dog(Animal):
    def bark(self) -> str:
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())
print()



# 2. COMPOSITION (Strong Has-a) - "Owns-a"

print("--- 2. Composition ---")

class Room:
    def __init__(self, name: str):
        self.name = name

class House:
    def __init__(self):
        # House creates and completely owns the lifetime of these Room objects
        self.rooms = [Room("Kitchen"), Room("Bedroom")]

my_house = House()
for room in my_house.rooms:
    print(f"Room created: {room.name}")
print()



# 3. AGGREGATION (Weak Has-a) - "Contains-a"

print("--- 3. Aggregation ---")

class Book:
    def __init__(self, title: str):
        self.title = title

class Library:
    def __init__(self, books: list[Book] = None):
        self.books = books if books else []

# Books are created independently outside
book1 = Book("1984")
my_library = Library([book1])
print(f"Library has book: {my_library.books[0].title}")

# Destroying the library container
del my_library  
print(f"Book still exists after library deletion: {book1.title}")
print()


# 4. ASSOCIATION (Knows-a) - "Linked-to"

print("--- 4. Association ---")

class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []

class Order:
    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        # Keep track of structural links bidirectionally
        customer.orders.append(self)

alice = Customer("Alice")
order_1 = Order(101, alice)

print(f"Customer {alice.name} has order ID: {alice.orders[0].order_id}")
print(f"Order 101 belongs to customer: {order_1.customer.name}")
print()



# 5. DEPENDENCY (Uses-a) - "Temporary"

print("--- 5. Dependency ---")

class Printer:
    def print_page(self, text: str):
        print(f"Printing: {text}")

class ReportGenerator:
    def __init__(self, content: str):
        self.content = content

    def output_report(self, printer_device: Printer):
        # The Printer reference is used temporarily inside this method frame
        printer_device.print_page(self.content)

my_printer = Printer()
quarter_report = ReportGenerator("Q1 Financials: Excellent")
quarter_report.output_report(my_printer)
print()



# 6. REALIZATION (Implements) - "Contract"

print("--- 6. Realization ---")

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class GCashPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ₱{amount} via GCash.")
        return True

gateway = GCashPayment()
success = gateway.process_payment(250.75)
print(f"Payment Status: {success}")

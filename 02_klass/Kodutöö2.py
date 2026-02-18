class Flight:
    def __init__(self, flight_number, destination, capacity, ticket_price):
        self.flight_number = flight_number
        self.destination = destination
        self.capacity = capacity          # maksimaalne kohtade arv
        self.ticket_price = ticket_price  # ühe pileti hind
        self.booked_seats = 0             # praegu broneeritud

    def book_seats(self, number):
        available = self.capacity - self.booked_seats
        if number <= available:
            self.booked_seats += number
            print(f"{number} kohta broneeritud lennule {self.flight_number}.")
        else:
            print(f"Ei saa broneerida {number} kohta! Vabu kohti on ainult {available}.")

    def flight_status(self):
        free_seats = self.capacity - self.booked_seats
        revenue = self.booked_seats * self.ticket_price
        print(f"\nLend {self.flight_number} sihtkohaks {self.destination}")
        print(f"Broneeritud kohti: {self.booked_seats}")
        print(f"Vabu kohti: {free_seats}")
        print(f"Piletitulu: {revenue} €")
        
# Lennu andmed
flight1 = Flight("BT101", "London", 149, 120)
flight2 = Flight("BT205", "Malaga", 149, 180)

# Broneeringud
flight1.book_seats(80)
flight1.book_seats(30)
flight2.book_seats(140)
flight2.book_seats(10) 

# Lennu seisud
flight1.flight_status()
flight2.flight_status()
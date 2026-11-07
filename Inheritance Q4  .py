'''
Q4. Vehicle Rental System | Intermediate
Create a base class Vehicle with brand, model, and daily rental rate. Implement calculate_rent(days). Derive Car,
which adds a fixed insurance fee of Rs. 1,000 per rental, and Bike, which applies a 10% discount to the base
rental amount. Override calculate_rent() and reuse the parent implementation with super(). Reject rental
durations of zero or fewer days. Test both vehicle types for a three-day rental
'''
class Vehicle:
    def __init__(self, brand, model, daily_rental_rate):
        self.brand = brand
        self.model = model
        self.daily_rental_rate = daily_rental_rate

    def calculate_rent(self, days):
        if days <= 0:
            print("Rental duration must be greater than zero.")
            return None
        return self.daily_rental_rate * days


class Car(Vehicle):
    def __init__(self, brand, model, daily_rental_rate):
        super().__init__(brand, model, daily_rental_rate)
        self.insurance_fee = 1000

    def calculate_rent(self, days):
        base_rent = super().calculate_rent(days)
        if base_rent is None:
            return None
        return base_rent + self.insurance_fee

class Bike(Vehicle):
    def __init__(self, brand, model, daily_rental_rate):
        super().__init__(brand, model, daily_rental_rate)

    def calculate_rent(self, days):
        base_rent = super().calculate_rent(days)
        if base_rent is None:
            return None
        return base_rent - (base_rent * 0.1)  # Apply 10% discount

# --- Demo ---
print("--- Vehicle Rental System ---")
car1 = Car("Toyota", "Corolla", 2000)
bike1 = Bike("Yamaha", "R15", 500)
print(f"Car Rental for 3 days: Rs. {car1.calculate_rent(3)}")
print(f"Bike Rental for 3 days: Rs. {bike1.calculate_rent(3)}")

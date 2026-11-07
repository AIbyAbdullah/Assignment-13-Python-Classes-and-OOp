'''
Q6. Checkout Discount Calculator | Intermediate
Create RegularCustomer, PremiumCustomer, and VIPCustomer classes, each implementing
final_price(amount). Apply discounts of 5%, 10%, and 20%, respectively. Write print_receipt(customer, amount)
so that it works with any customer type. For a bill of Rs. 10,000, show the final amount for each type. Reject
negative bill amounts. Extension: Add GoldCustomer with a 15% discount without modifying print_receipt().
'''
# Q6.py - Checkout Discount Calculator

class RegularCustomer:
    def final_price(self, amount):
        if amount < 0:
            print("Invalid bill amount! Cannot be negative.")
            return None
        return amount * 0.95  # 5% discount

class PremiumCustomer:
    def final_price(self, amount):
        if amount < 0:
            print("Invalid bill amount! Cannot be negative.")
            return None
        return amount * 0.90  # 10% discount

class VIPCustomer:
    def final_price(self, amount):
        if amount < 0:
            print("Invalid bill amount! Cannot be negative.")
            return None
        return amount * 0.80  # 20% discount

class GoldCustomer:
    def final_price(self, amount):
        if amount < 0:
            print("Invalid bill amount! Cannot be negative.")
            return None
        return amount * 0.85  # 15% discount

def print_receipt(customer, amount):
    final_amount = customer.final_price(amount)
    if final_amount is not None:
        # print(f"Final amount after discount: Rs. {final_amount:.2f}")  #.2f print 2 point after decimal exp: 9500.00
        #    OR when you print name of custmer class and final amount
        print(f"Customer: {customer.__class__.__name__}, Final: Rs.{final_amount:.2f}")

# --- Demo ---
print("--- Bill: Rs. 10000 ---")
bill = 10000
print_receipt(RegularCustomer(), bill)
print_receipt(PremiumCustomer(), bill)
print_receipt(VIPCustomer(), bill)

print("\n--- Extension + Rejected Test ---")
print_receipt(GoldCustomer(), bill)
print_receipt(RegularCustomer(), -500)

'''
15% nikalne ka formula
final_amount = amount - (amount * 0.15)
exp
amount = 10000
final_amount = 10000 - (10000 * 0.15) = 100
final_amount = 10000 - 1500 = 8500


how 0.15 is calculated 
15% = 15/100 = 0.15
'''


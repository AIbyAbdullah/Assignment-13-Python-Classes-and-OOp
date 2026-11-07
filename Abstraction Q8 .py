'''
Q8. Payment Gateway | Intermediate
Define an abstract PaymentMethod class with abstract methods pay(amount) and refund(amount). Implement
CardPayment, WalletPayment, and BankTransferPayment. Each method must display the payment method,
transaction type, and amount. Validate that transaction amounts are positive. Write process_transaction(method,
amount) to call pay() for any supported payment method. Extension: Add a new payment method without
changing process_transaction().
'''
# Q8.py - Payment Gateway

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CardPayment(PaymentMethod):
    def pay(self, amount):
        if amount <= 0:
            print("Card Payment Failed: Amount must be positive")
            return
        print(f"[Card] Pay: Rs.{amount} paid via Card")

    def refund(self, amount):
        if amount <= 0:
            print("Card Refund Failed: Amount must be positive")
            return
        print(f"[Card] Refund: Rs.{amount} refunded to Card")

class WalletPayment(PaymentMethod):
    def pay(self, amount):
        if amount <= 0:
            print("Wallet Payment Failed: Amount must be positive")
            return
        print(f"[Wallet] Pay: Rs.{amount} paid via Wallet")

    def refund(self, amount):
        if amount <= 0:
            print("Wallet Refund Failed: Amount must be positive")
            return
        print(f"[Wallet] Refund: Rs.{amount} refunded to Wallet")

class BankTransferPayment(PaymentMethod):
    def pay(self, amount):
        if amount <= 0:
            print("Bank Transfer Failed: Amount must be positive")
            return
        print(f"[Bank Transfer] Pay: Rs.{amount} paid via Bank Transfer")

    def refund(self, amount):
        if amount <= 0:
            print("Bank Transfer Failed: Amount must be positive")
            return
        print(f"[Bank Transfer] Refund: Rs.{amount} refunded to Bank")

# Extension - Bina process_transaction change kiye
class JazzCashPayment(PaymentMethod):
    def pay(self, amount):
        if amount <= 0:
            print("【entity-JazzCash】 Failed: Amount must be positive")
            return
        print(f"【JazzCash】Pay: Rs.{amount} paid via 【JazzCash】")

    def refund(self, amount):
        if amount <= 0:
            print("【entity-JazzCash】 Refund Failed: Amount must be positive")
            return
        print(f"[JazzCash] Refund: Rs.{amount} refunded to JazzCash")

def process_transaction(method, amount):
    method.pay(amount) # Polymorphism yahan hai

# --- Demo ---
print("--- Payment Gateway Test ---")
process_transaction(CardPayment(), 5000)
process_transaction(WalletPayment(), 2000)
process_transaction(BankTransferPayment(), 10000)

print("\n--- Refund Test ---")
CardPayment().refund(1000)

print("\n--- Extension + Rejected Test ---")
process_transaction(JazzCashPayment(), 3000)
process_transaction(CardPayment(), -500) # Rejected
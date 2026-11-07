'''
Q2. Secure Bank Account | Intermediate
Create a BankAccount class with a public account holder name, private __balance, and private __pin. Implement
deposit(amount), withdraw(amount, pin), and get_balance(pin). Reject zero or negative deposits, withdrawals
exceeding the available balance, and incorrect PINs. Demonstrate a successful deposit, a successful withdrawal,
and two rejected operations. Extension: Explain why double underscores do not provide true security.
'''
'''
return or return None , both are same, but return None is more explicit and clear.
It indicates that the function is intentionally returning nothing, which can be helpful for readability and understanding the code's intent.
'''

class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder # public
        self.__balance = balance             # private
        self.__pin = pin                     # private

    def deposit(self, amount):
        if amount <= 0:
            print(f"Deposit Failed: Amount {amount} must be positive")
            return None
        self.__balance += amount
        print(f"Deposit Success: {amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Withdrawal Failed: Incorrect PIN")
            return None
        if amount <= 0:
            print("Withdrawal Failed: Amount must be positive")
            return None
        if amount > self.__balance:
            print(f"Withdrawal Failed: Insufficient balance. You have {self.__balance}")
            return None
        
        self.__balance -= amount
        print(f"Withdrawal Success: {amount} withdrawn. Remaining: {self.__balance}")

    def get_balance(self, pin):
        if pin != self.__pin:
            print("Balance Check Failed: Incorrect PIN")
            return None
        
        return self.__balance

# --- Demo ---
print("--- Account Created ---")
acc1 = BankAccount("Ali", 1000, "1234")
acc2 = BankAccount("Sara", 500, "9999")

# 1. Successful deposit
print("\n1. Successful Deposit:")
acc1.deposit(-500)

# 2. Successful withdrawal
print("\n2. Successful Withdrawal:")
acc1.withdraw(300, "1234")

# 3. Rejected Operation 1: Wrong PIN
print("\n3. Rejected (Wrong PIN):")
acc1.withdraw(100, "0000")

# 4. Rejected Operation 2: More than balance + Negative deposit
print("\n4. Rejected (Insufficient Balance & Negative Deposit):")
acc1.withdraw(5000, "1234")
acc2.deposit(-100)

# Final balance check
print("\nFinal Balance:")
print(f"Ali's Balance: {acc1.get_balance('1234')}")


class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance 
    
  def deposit(self, amount):
    self.balance += amount
    print(f"Deposit of {amount} into the account. New balance: {self.balance}")

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds.")
    else:
      self.balance -= amount
      print(f"Withdrawal of {amount} from the account. New balance: {self.balance}")

  def display_balance(self):
    print(f"Current balance: {self.balance}")

julia = BankAccount('Julia', 'Pereira', 71728, 'savings account', 237, 56000)

julia.deposit(96)
julia.withdraw(25)
julia.display_balance()

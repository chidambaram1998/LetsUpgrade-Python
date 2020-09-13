class bankAccount():
  def __init__(self,ownerName,Balance):
    self.ownerName = ownerName
    self.Balance = Balance

  def deposit(self):
    amount = float(input("Enter amount to be deposited: ")) 
    self.Balance += amount 
    print("%.2fRs. Deposited in the bank account of %s"%(amount, self.ownerName))
  
  def withdraw(self): 
    amount = float(input("Enter amount to be withdrawn: ")) 
    if self.Balance >= amount: 
      self.Balance -= amount 
      print("%s Withdrew %f"%(self.ownerName,amount)) 
    else: 
      print("Insufficient balance")

  def checkBal(self):
    print("Current Balance:",self.Balance)

b = bankAccount("chidu", 0)
b.deposit()
b.withdraw()
b.checkBal()

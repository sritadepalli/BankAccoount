class Bankaccount:
    def ___init___(account_holdername,account_number):
        self.account_holdername=account_holdername()
        self.account_number=account_number()
    def __init__(self):
        self.balance=700
    def deposit(self):
        amount=float(input("enter the amount to be deposit:"))
        self.balance+=amount
        print("Your deposit is successful..")
        print(f'deposited_amount: ${amount} and current balance: ${self.balance}')
    def withdraw(self):
         amount=float(input("Enter the amount to withdraw"))
         if(self.balance >= amount):
             self.balance-=amount
             print("withdrawl is successful..")
             print(f'withdrawan amount: ${amount} and current balance: ${self.balance}')
         else:
             print("!!insufficient balance!! \n SORRY..Withdrawl cancelled!")
    def display(self):
        print(f'current balance: ${self.balance}')
        
        
if __name__=='__main__':
    account_holdername=input("enter account_holdername:")
    print('account_holdername:',account_holdername)
    account_number=input("enter account_number:")
    print("account_number:",account_number)
    account=Bankaccount()
    while(True):
       print("Press 1 for deposit")
       print("Press 2 for withdraw")
       print("Press 3 for display")   
       a=input()
       if a not in ['1','2','3']:
           continue
       else:
           a=int(a)
           
       if a==1:
           account.deposit()
       elif a==2:
           account.withdraw()
       elif a==3:
           account.display()
       else:
           print("not valid")
           
       print("press c to continue and q to quit")
       b=input()
       if b=="c":
           continue
       if b=="q":
           exit()

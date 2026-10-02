

class ATM:
    # Constructor? - Function inside the class
    #              - But has  super power to execute without call as object.
    #              - Constructor executed automatically without calling .  
    def __init__(self):
        self.pin = ''
        self.balance= 0
        print("I am executed.")
        self.menu()

    def menu(self):
        uinpt =input(("""Hi, how can i help you?
        1. Press 1 to create Account .
        2. Press 2 to change pin .
        3. Press 3 to check banalnce .
        4. press 4 to withdraw .
        5. Anythng else to exit ."""))
        if uinpt=='1':
            self.create_account()
        elif uinpt == '2':
            self.change_pin()
        elif uinpt == '3':
            self.check_balance()
        elif uinpt == '4':
            self.withdraw()
        elif uinpt=='5':
            print("Exiting .......")
            pass
        else: 
            print("Enter Number from 1 to 5 : ")
            self.menu()


    def create_account(self):
        user_pin=input("Enter your pin: ")
        self.pin = user_pin 
        user_balance=int(input("Enter amount (digit) :  "))
        self.balance=user_balance
        print("Account created successfully.")
        self.menu()

    def change_pin(self):
        old_pin=input("Enter your old pin: ")
        if self.pin==old_pin :
            new_pin=input("Enter your new pin: ")
            newpin= input("Enter your pin again: ")
            if(new_pin==newpin):
                self.pin=new_pin
                print("Your pin change successfully. ")
                self.menu()
            else:
                print("Enter new pin correctly. ")
                self.change_pin()
        else: 
            print("Pin matched . ")
            self.change_pin()

    def check_balance(self):
        user_pin=input ("Enter your pin: ")
        if (self.pin==user_pin):
            print("Your balance is : ",self.balance)
            self.menu()
        else: 
            print("Inputed pin is wrong. ")
            self.check_balance ()

    def amount(self):
        w_amount=int(input("Enter amount to withdraw: "))
        return w_amount

    def withdraw ( self ):
        user_pin = input ("Enter your pin : ")
        if (user_pin == self.pin):
            w_amount= self.amount()
            if(w_amount <= self.balance):
                self.balance-=w_amount
                print("Withdrawal successful. ")
                self.menu()
            else:
                print ("Enter less amount:  ")
                self.withdraw()
        else:
            print("wrong pin.")
            self.withdraw()



object = ATM()

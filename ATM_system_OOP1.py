

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
        if user_balance >= 0:
            self.balance = user_balance
        else :
            self.create_account(self)
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
            print("Pin doesnot matched .")
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
        try:
            w_amount = int(input("Enter amount to withdraw: "))
            return w_amount
        except ValueError:
            print("Please enter a valid number.")
            return self.amount()    


    def withdraw ( self ):
        user_pin = input ("Enter your pin : ")
        if (user_pin == self.pin):
            w_amount= self.amount()
            if w_amount > 0 and w_amount <= self.balance:
                self.balance-=w_amount
                print("Withdrawal successful. ")
                self.menu()
            else:
                print("Enter amount correctly.")
                print ("Enter less amount:  ")
                self.withdraw()
        else:
            print("wrong pin.")
            self.withdraw()


object = ATM()


'''# ---------Methods Vs Functions-------------#

# Inside a class created function isnot independent so we named it function
# even though it's a function.   Out side of classs a function 
# isnot dependent it's independent . so that's it. '''

l= [1,2,3,4]
len (l)        # Function - cause it is outside the list class .
l.append(4)   # Method - cause it is inside the list class .
               # Append implemented inside the list class . That's why it's method. 
'''#--------------class Diagram----------------#
    --------------------------------
   |    class name                 |
   |-------------------------------|
   |   Data / variable/ attribute  |
   |  - pin/ + balance             |
   |-------------------------------|
   |    Method                     |
   |  Menu/ Create pin/- Change pin|
   | +  Check balance              |
   | + withdraw                    |
   |-------------------------------|
   # + => Public = outside the class 
   # - => private = That particular thing isnot visible outside the class.'''
   
# ----------Magic Methods-/-Duncer Methods / Constructor ---------------#
'''  Magic Method -- Special kind of method - has own super power.
Syntax:   __name__         Not necessary to call. It automatically trigger
         __init__          and execute.

    Constructor  -- A function define in the class . so it is a method . But it
            has a super power . As object created the method called automatically.
            No need the user action. Fixed things. Controll fixed.

    True benefit -- The execution of the programm have not to the user
            . It's automatic . But other method need o call then execute like pin_change,
                withdraw().

    Constructor - use to write configuration realted code / task. Database / network connection related code . 
Ex-- Allah is the programmer . Earth is  class -- Human is object but death 
        is constructor.        
'''
# -----------Self------------------------#
'''    Golden Rule of OOP-
           /     \
          /       \
      Class      Object---- The object follow the rules .
       /
All rules  written in it.

In class -- pin / balance-->  data / bariable/ 
         -- pin_change()/ withdraw()--> All are methods 

An object can only access the data bariable , method of the class that 
everything present inside the class.

Q. Can a method call the another method inside the class??
A. No- It's cannot -- Golden rull followed.

Each function inside the class has default parameter called self. 
It's actually act as object that actually follow the class instance. 


The self and object save in the same memory place. just follow the class or talk with all instance.
Self is the current object.
'''



class BankAccount:
    # private Attributes
    def __init__(self, Acc_Num, Acc_Balance):
        self.__Acc_Num: str = Acc_Num
        self.__Acc_balance: str = Acc_Balance

    # public methods
    def set_acc_num(self, Acc_num_value):
         self.__Acc_Num = Acc_num_value
         

    def set_balance(self, Acc_balance_value):
        self.__Acc_balance = Acc_balance_value
    
            

    @property
    def get_acc_num(self):
        return self.__Acc_Num

    @property
    def get_balance(self):
        return self.__Acc_balance

if __name__ == "__main__":
    A1 = BankAccount(
        Acc_Num = 12345,
        Acc_Balance = 1000
    )

    print(f"Output:")
    print(f"")
    print(f"Account 1")
    print(f"Account Number: [{A1.get_acc_num}]")
    print(f"Balance: [{A1.get_balance}]")
    End = True
    print("1 (set Account Number.), 2 (set Account Balance), 3 (End session)")
    while End == True:

        choice = input("Enter Choice: ")
    
        if choice == "1":
            Acc_num_value = input("Set Account Number to ")
            A1.set_acc_num(Acc_num_value)
            print(f"Account Number: [{A1.get_acc_num}]")
            print(f"Balance: [{A1.get_balance}]")

        elif choice == "2":
            Acc_balance_value = int(input("Set Balance to "))
            if Acc_balance_value < 0:
                print("Balance must not be negative.")
                End
            A1.set_balance(Acc_balance_value)
            print(f"Account Number: [{A1.get_acc_num}]")
            print(f"Balance: [{A1.get_balance}]")
        else:
            End = False

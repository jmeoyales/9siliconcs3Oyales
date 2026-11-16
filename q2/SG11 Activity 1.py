class Patient:
    """attribute"""
    def __init__(self,name, bill_amount):
        self.__name: str = name
        self.__bill_amount: float = bill_amount

    """Methods"""
    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self,bill_amount):
        self.__bill_amount = bill_amount
        return self.__bill_amount

    def calculate_bill(self):
        print()


class Senior(Patient):
    """overwrite"""
    def calculate_bill(self):
        
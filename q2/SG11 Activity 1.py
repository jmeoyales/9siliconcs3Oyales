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
        return self.get_bill_amount()

    def display_patient_type(self):
        return "regular patient"


class Senior(Patient):
    """overwrite"""
    def calculate_bill(self):
        final_bill = self.get_bill_amount() - (self.get_bill_amount() * 0.20)
        return final_bill
    def display_patient_type(self):
        return "Senior Patient"

class Philhealth(Patient):
    """overwrite"""
    def calculate_bill(self):
        final_bill = self.get_bill_amount() - (self.get_bill_amount() * 0.15)
        return final_bill
    def display_patient_type(self):
        return "PhilHealth Member"

"""instantiate"""

regular = Patient("Juan Dela Cruz", 15000)
senior = Senior("Maria Santos", 15000)
Phil = Philhealth("Pedro Reyes", 15000)

"""main"""
print("Hospital Billing System")
print("-------------------------")
print(f"Patient Name: {regular.get_name()}")
print(f"Patient Type: {regular.display_patient_type()}")
print(f"Original Bill: {regular.get_bill_amount()}")
print(f"Final Bill: {regular.calculate_bill()}")
print()
print(f"Patient Name: {senior.get_name()}")
print(f"Patient Type: {senior.display_patient_type()}")
print(f"Original Bill: {senior.get_bill_amount()}")
print(f"Final Bill: {senior.calculate_bill()}")
print()
print(f"Patient Name: {Phil.get_name()}")
print(f"Patient Type: {Phil.display_patient_type()}")
print(f"Original Bill: {Phil.get_bill_amount()}")
print(f"Final Bill: {Phil.calculate_bill()}")


class Digitalsafe:
    def __init__(self, safename: str = "", maxstorage: int = 0, username: str = "", passkey: str = "", compartments: int = 1):
        # Public attributes
        self.safename: str = safename
        self.maxstorage: int = maxstorage
    
        # Private attributes
        self.__Username: str = username
        self.__User_passkey: str = passkey
        self.__Available: bool = False
        self.__Compartments: int = compartments
        self.__files: str = ""

    # Checks user passkey for entry into safe
    def accesssafe(self, given_paskey: str) -> bool:
        if given_paskey == self.__User_passkey:
            print(f"[{self.safename}] Access granted.")
            return True
        else:
            print(f"[{self.safename}] Access not granted.")
            return False

    def addfile(self, filename: str) -> None:
        if self.__files == "":
            self.__files = filename
        else:
            self.__files += f", {filename}"
        self.__Available = True
        print(f"[{self.safename}] Stored file: {filename}")

    def take_files(self, filename: str) -> str:
        if not self.__Available:
            return ""
        taken = self.__files
        self.__files = ""
        self.__Available = False  # will become false when it is empty
        return taken

    def get_compartments(self) -> int:
        """collects all compartments in the safe"""
        return self.__Compartments

    def display_info(self) -> None:
        file_list = self.__files if self.__files else "no files to display :( "
        print(f"Safe name: {self.safename} | Capacity : {self.maxstorage} | Compartments:  {self.__Compartments} | files: {file_list}")


class DigitalSafeManager:
    """
    Manages all safes under its registry
    """
    def __init__(self, manager_name: str = ""):
        self.m_name: str = manager_name
        self.__safe_list: list = []  # stores the references

    def register_safe(self, safe_object: Digitalsafe) -> None:
        """stores the reference to a digtal safe object"""
        if isinstance(safe_object, Digitalsafe):
            self.__safe_list.append(safe_object)
            print(f"Manager '{self.m_name}' safe registered: {safe_object.safename}")
        else:
            print("must be an instance of a digital safe.")

    def total_compartments(self) -> int:
        """calculates all compartments throughout the registry of the manager"""
        total = sum(safe.get_compartments() for safe in self.__safe_list)
        return total

    def show_all_managed_safes(self) -> None:
        """goes through all safes in registry and shows the methods"""
        print(f"\n--- SAFES MANAGED BY: {self.m_name} ---")
        if not self.__safe_list:
            print("No safes currently in registry")
            return
        
        for safes, safe in enumerate(self.__safe_list, start=1):
            print(f"{safes}. ", end="")
            safe.display_info()
        print(f"All System Compartments: {self.total_compartments()}")


class Biometric_safe(Digitalsafe):
    def __init__(self, safename = "", maxstorage = 0, username = "", passkey = "", compartments = 1, biometric = "", user_bio = "", input_bio = ""):
        super().__init__(safename, maxstorage, username, passkey, compartments)

        """Self stuff for child class of digital safe"""
        self.Biometric = biometric
        self.Log_book = []
        self.biometric_user = user_bio

    """methods"""
    def addlog(self,biometric: str) -> str:
        self.Log_book.append(biometric)
        

    def verify_biometric(self,biometric: str, input_bio: str, date_time: str) -> bool:
        print(f"input Biometric: {biometric}")
        if input_bio == biometric:
            biometricsafe.addlog(biometric)
            biometricsafe.addlog(date_time)
            print("access granted.")
            
            


if __name__ == "__main__":


    # instatiating an instance of biometric safe
    biometricsafe = Biometric_safe(
        safename = "biosafe",
        maxstorage = 1000,
        username = "Oyales",
        compartments = 10,
        passkey = "12345jon",
        biometric = "0001index",
        
    )

    #testing inherited traits
    print(biometricsafe.display_info())
    print("Optional access safe with biometric: ")
    biometricsafe.verify_biometric(biometric= "0001index", input_bio= "0001index", date_time= "09/23/26 | 10:20 pm")
    print(biometricsafe.Log_book)
    
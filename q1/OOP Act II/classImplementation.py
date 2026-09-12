class Digitalsafe:
    def __init__(self, safename: str = "", maxstorage: int = 0, username: str = "", passkey: str = "", compartments: int = 1):
        # Public
        self.Safename: str = safename
        self.maxstorage: int = maxstorage
        # Private
        self.__Username: str = username
        self.__User_passkey: str = passkey
        self.__Available: bool = False
        self.__Compartments: int = compartments
        self.__files: dict[int, list[str]] = {i: [] for i in range(1, self.__Compartments + 1)}

    def total_file_count(self) -> int:
        return sum(len(files) for files in self.__files.values())

    def accesssafe(self, given_paskey: str) -> bool:
        if given_paskey == self.__User_passkey:
            print("Access granted")
            return True
        else:
            print("Access denied")
            return False
        
    def addfile(self, filename: str, compartment: int = 1) -> None:
        # Checks if compartment exists
        if compartment not in self.__files:
            print(f"Inputted compartment as destination {compartment} does not exist")
            return

        # Checks if input will exceed storage capacity
        if self.total_file_count() >= self.maxstorage:
            print(f"Cannot store file {filename}: exceeded storage capacity of {self.maxstorage}")
            return

        self.__files[compartment].append(filename)
        self.__Available = True
        print(f"Successfully added file to digital safe {self.Safename}")

    def take_files(self, filename: str, compartment: int = 1) -> str:
        if compartment in self.__files and filename in self.__files[compartment]:
            self.__files[compartment].remove(filename)
            if self.total_file_count() == 0:
                self.__Available = False
            return filename
        else:
            print("File was not found in destination")
            return ""

    def display_info(self) -> None:
        files_present = "yes" if self.__Available else "no"
        print(f"\nSafe name: {self.Safename} | Total storage used: {self.total_file_count()}/{self.maxstorage} | Files available: {files_present}")
        print(f"Owner: {self.__Username}")
        print("Compartments:")
        for comp_num, files_list in self.__files.items():
            content = ", ".join(files_list) if files_list else "No files present"
            print(f"  Compartment {comp_num}: {content}")

    @staticmethod
    def create_safe() -> "Digitalsafe":
        print("\n Make a safe")
        safename = input("Enter safename: ")
        maxstorage = int(input("Enter max storage capacity: "))
        username = input("Enter username: ")
        passkey = input("Enter a passkey you will use: ")
        compartments = int(input("Enter number of compartments: "))
        
        return Digitalsafe(safename, maxstorage, username, passkey, compartments)

    @staticmethod
    def initialize_safe_TEST():
        # Object 1
        safe1 = Digitalsafe(
            safename="Personal Safe", 
            maxstorage=5, 
            username="van lester", 
            passkey="vault12390", 
            compartments=2
        )
        
        # Object 2
        safe2 = Digitalsafe(
            safename="Corporate Vault", 
            maxstorage=100, 
            username="BIRON", 
            passkey="larper", 
            compartments=5
        )
        
        print("\nInitial state of objects:")
        safe1.display_info()
        safe2.display_info()
        
        print("\nModification of object 1:")
        safe1.addfile("passwords.txt", compartment=1)
        safe1.addfile("tax_2026.pdf", compartment=2)
        
        print("\nAfter modification of object 1:")
        safe1.display_info()
        
        print("\nProof of object 2's independence:")
        safe2.display_info()
        return safe1, safe2


    


# Main
if __name__ == "__main__":
    while True:
        print("\n---------- Choices:")
        print("1. Demonstrate class")
        print("2. Create safe")
        print("3. Exit")
        
        choice = input("Enter choice: ").strip()

        if choice == "1":
            Digitalsafe.initialize_safe_TEST()
        elif choice == "2":
            new_safe = Digitalsafe.create_safe()
            print("\nSafe successfully created!")
            new_safe.display_info()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")
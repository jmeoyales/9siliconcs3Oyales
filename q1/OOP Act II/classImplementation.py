

class Digitalsafe:
    def __init__(self, safename: str = "", maxstorage: int = 0, username: str = "", passkey: str = ""):
    # public
        self.Safename: str = safename
        self.maxstorage: int = maxstorage
    
    # private
        self.__Username: str = username
        self.__User_passkey: str = passkey
        self.__Available: bool = False
        self.__Compartments: int = 1
        self.__files:  dict[int, list[str]] = {i: [] for i in range(1, self.__Compartments + 1)}


#fucntion to open safe to user
    def total_file_count(self) -> int:
        return sum(len(files) for files in self.__files.values())

    
    def accesssafe(self, given_paskey: str,) -> bool:
        if given_paskey == self.__User_passkey:
            print("access granted")
            return True
        else:
            print("access not granted")
            return False

    def addfile(self, filename: = str, compartment: int = 1) -> None:
        #checks if compartment inputted as destination exists
        if compartment not in self.__files:
            print("Inputted compartment " + compartment +"destination does not exist")
        #checks if input will exceed storage capacity
        if self.__files >= self.maxstorage:
            print("Cannot store" + filename +" reached max storage of " + self.maxstorage )
            return
        #declares if a file is available
        self.__files.append(filename)
        self.__Available = True
        print("Succesfully added " + filename)

    
    def take_files(self, filename) -> str:
        if filename in self.__files:    
            self.__files.remove(filename)
            if not self.__files:
                self.__Available = False
            return filename
        else:
            print("file "+ filename + " was not found")
            return ""

    def display_info(self) -> None:
        files_present = "yes" if self.__Available == "no"
        files_list = "| ". join(self.__files) if self.__files 


if __name__ == "__main__":
    safe1 = Digitalsafe("Personal Safe", 5, "van lester", "vault12390")
    safe2 = Digitalsafe("Corporate Vault", 100, "BIRON", "admin99")

    print("=== BEFORE ACTION ===")
    print("Object 1 Initial State:")
    safe1.display_info()
    print("\nObject 2 Initial State:")
    safe2.display_info()

    print("\n=== PERFORMING ACTIONS ON OBJECT 1 ONLY ===")
    safe1.addfile("passwords.txt")
    safe1.addfile("tax_2026.pdf")

    print("\n=== AFTER ACTION ===")
    print("Object 1 Updated State:")
    safe1.display_info()
    print("\nObject 2 Unchanged State:")
    safe2.display_info()



    
    
         




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
        self.__files: str = ""


#fucntion to open safe to user
    def accesssafe(self, given_paskey: str,) -> bool:
        if given_paskey == self.__User_passkey:
            print("access granted")
            return True
        else:
            print("access not granted")
            return False

    def addfile(self, filename = str) -> None:
        #adds files
        if self.__files == "":
            self.__files = filename
        else:
            self.__files += f"{filename}"
        #changes availablity of files to true meaning there are files
        self.__Available = True
        print("you have stored"+ filename)

    def take_files(self, filename) -> str:
        if not self.__Available:
            return ""
        taken = self.__files
        self.__files = ""
        self.__Available = False  # Set back to False since storage is now empty
        return taken

    def display_info(self) -> None:
        files_present = "yes there are files present" if self.__Available else "no there are no files"
        file_list = self.__files if self.__files else "none"
        print(f"Safe name: {self.Safename} | Capacity:  {self.maxstorage} | ")


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



    
    
         


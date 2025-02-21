class details:
    def __init__(self,firstName,middleName,lastName,address="Hyderabad"):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.address = address

    def get_fullname(self):
        print(f"{self.firstName}{self.middleName}{self.lastName}")
    
    def get_address(self):
        print(self.address)

obj1 = details("Kundanika"," ","Madireddy") 
obj1.get_fullname()
obj2 = details("Uday","Kumar","V","Kakinada")
obj2.get_address()


        
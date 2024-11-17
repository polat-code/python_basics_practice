
class User:
    def __init__(self,name: str,surname: str ,email: str) -> None:
        self.name = name
        self.surname = surname
        self.email = email
    
    def __eq__(self, value: "User") -> bool:
        if isinstance(value, User):
            return self.name == value.name and self.surname == value.surname and self.email == value.email
        return False

    def greeting(self) -> str:
        return f"Hello {self.name}! Welcome to {self.surname} {self.email}!"



user1 = User("Özgürhan","Polat","email@mail.com")

# Extend class

class Customer(User):
    def __init__(self, name: str, surname: str, email: str) -> None:
        super().__init__(name, surname, email)
        self.balance = 0

    def set_balance(self,balance : int) -> None:
        self.balance = balance

    def greeting(self) -> str:
        return f"Hello {self.name}! Welcome to {self.surname} {self.email} and balance is {self.balance}!"

    
    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

customer1 = Customer("özgürhan","polat","email@mail.com")
customer1.set_balance(100)
print(customer1.greeting())
print(customer1)

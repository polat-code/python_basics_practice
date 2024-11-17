
class Item:
    price_rate = 0.8
    all = []
    def __init__(self,name: str,price : float,quantity : int = 0) -> None:
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.price_rate

    # Class level method (static)
    @classmethod
    def instantiate_from_csv(cls):

    def __repr__(self):
        return f"Name : {self.name},Quantity : {self.quantity}, Price: {self.price}"

item1 = Item("Özgürhan",100,2)
item2 = Item("Fatih",1020,5)
item3 = Item("Kadir",1050,1)
item4 = Item("Fatih",140,3)
item5 = Item("Mehmet",100,5)
item6 = Item("Ahmet",100,9)

#print(Item.all)


#print(int(item1.calculate_total_price()))
#print(item2.calculate_total_price())
#item1.apply_discount()
#print(item1.price)

#item1.price_rate = 0.7
#item1.apply_discount()
#print(item1.price)







#print(Item.__dict__) # Class level attribute (Magical Attribute)
#print(item1.__dict__)  # Instance level attribute
#print(Item.price_rate) # Class Level Attribute


#print(item1.__str__())





class shopping_cart:
    def __init__(self):
        self.items = {}

    def add_item(self , name , price):
        self.items[name] = price
    
    def get_total(self):
        return sum(self.items.values())
    
    def most_expensive(self):
        return max(self.items, key = self.items.get)
    
    def remove_item(self, name):
        try :
            del (self.items[name])
        except KeyError:
            print(f"{name} is not in the records.")

    


instance1 = shopping_cart()
instance1.add_item("potato", 10)
instance1.add_item("tomato" , 20)
instance1.add_item("onion", 15)
print(instance1.items)

print(instance1.most_expensive())
print(instance1.get_total())
print(instance1.remove_item("potato"))

print(instance1.items)

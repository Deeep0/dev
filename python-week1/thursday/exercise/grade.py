class Gradebook:
    def __init__ (self):
        self.data = {}

    def add_student(self, name , grade):
        self.data[name] = grade

    def get_average(self):
        return sum(self.data.values()) / len(self.data)

    def top_student(self):
        return max(self.data, key = self.data.get)

    def remove_student(self, name):
        try :
            del self.data[name]
        except KeyError:
            print(f"{name} not found in gradebook")



instance1 = Gradebook()
instance1.add_student("alex", 20)
instance1.add_student("dee" ,30)
print(instance1.top_student())
print(instance1.data)
instance1.remove_student("alex")
print(instance1.data)
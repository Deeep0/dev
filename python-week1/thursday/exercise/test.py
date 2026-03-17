class Employee :
    def __init__ (self, name , age , salary):
        self.name = name
        self.age = age
        self.salary = salary

    def salary_tax():
        return (salary * 1.2)
    

emp1 = Employee("alex", 20 , 1000)

emp2 = Employee("bat", 22 , 1200)
print(emp1.name)
print(emp2.pay)
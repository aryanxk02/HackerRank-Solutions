class Employee:
    increment = 5
    def __init__(self, fname, lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def increase(self):
        self.salary = int(self.salary * self.increment)
    @classmethod
    def bonus_increment(cls, amount):
        cls.increment = amount
aryan = Employee('aryan', 'singh', 1000000)
#harry = Employee('harry', 'singh',50000)
print(aryan.salary)
#aryan.increase()
#print(aryan.salary)
#print('-------')
#print(harry.salary)
#harry.increase()
#print(harry.salary)
print('-------')
Employee.bonus_increment(2)
aryan.increase()
print(aryan.salary)

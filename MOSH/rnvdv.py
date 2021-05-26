class Person:
    def __init__(self, name):
        self.name = name
    def first_function(self):
        print('hi, I am', self.name)

obj=Person("aryan")
x=obj.first_function()
print(x)


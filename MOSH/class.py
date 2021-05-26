class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('hi aryan i hope you are doing well, the coordinates of point are', self.x, self.y)
    def draw(self):
        print('draw')
obj1 = Point(10,22)
print(obj1.x, obj1.y)
blah=obj1.move()
print(blah)
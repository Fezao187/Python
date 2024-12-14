### Classes
class Fruit:
    def __init__(self, color, name):
        self.name = name
        self.color = color
    def __str__(self):
        print("My " +self.name + "'s color is: " + self.color )

my_fruit = Fruit('Red', 'Apple')
print(my_fruit.color)
my_fruit.__str__()
my_fruit.color = 'blue'
print(my_fruit.color)
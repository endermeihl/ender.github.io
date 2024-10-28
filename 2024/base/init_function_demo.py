class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk'
    def sing(self):
        print(self.sound)

b = SongBird()
b.eat()
b.sing()

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self,size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    size = property(get_size,set_size)

r = Rectangle()

class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')
    smeth = staticmethod(smeth)
    @classmethod
    def cmeth(cls):
        print('This is a class method of',cls)
    cmeth = classmethod(cmeth)

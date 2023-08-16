class Car:
    def __init__(self, color):
        self.color = color
        self.__speed = 60
        self._made = 'iran'

    def connect(self):
        print("connecting with {0}s".format(self.__speed))


c = Car("red")

# print(_c.__speed)
print("----------------------------------------------------------------")
print(c.__dict__)
c.color = 'black'
print(c.__dict__)

print('----------------------------------------------------------------')
c.__speed = 30
print(c.__dict__)
print('----------------------------------------------------------------')
c.__speed = 10000
c._made =  "usa"
print(c.__dict__)
print('----------------------------------------------------------------')
c._made = "duatchland"
print(c.__dict__)
print(c._Car__speed)

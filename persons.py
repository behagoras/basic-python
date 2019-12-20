
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        # super().__init__()

    def say_hello(self):
        print('Hello, my name is {} and I am {} years old'.format(self.name, self.age))


if __name__ == "__main__":
    person1 = Person('david',30)
    person1.say_hello()        
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def show_information(self):
        print(f'{self.name} is {self.age} y.o.')
        
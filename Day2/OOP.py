class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hi I'm {self.name}!")
        
p = Person("Silambazhagii")
p.greet()
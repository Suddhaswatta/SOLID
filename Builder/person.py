class Person:
    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.date_of_birth = None
        
    def __str__(self) -> str:
        return f'{self.name} was born in the year {self.date_of_birth} , works as a {self.position}'    
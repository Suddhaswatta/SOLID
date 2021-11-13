from abc import ABC, abstractmethod


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None
        
    def __str__(self) -> str:
        return f'Person {self.name} works as {self.position} '
    
    @staticmethod
    def create():
        return PersonBuilder()

class PersonBuilder:
    
    def __init__(self):
        self.person = Person()
        
    def build(self):
        return self.person
    
    def works_as(self,job):
        self.person.position = job
        return self
    
    def known_as(self,name):
        self.person.name = name
        return self
   
personA = Person.create()\
            .known_as("Eve")\
                .works_as("Scrum Master")\
                    .build()
                    
personB = Person.create()\
            .known_as(name="Adam")\
                .works_as(job="Developer")\
                    .build()        
print(personA)
print(personB)
    



from abc import ABC, abstractmethod


class Person:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.position = None
        self.date_of_birth = None
        
    def __str__(self) :
        return f'Born in {self.date_of_birth} ,{self.first_name} {self.last_name}, works as : {self.position}'
    
    @staticmethod
    def create():
        return PersonBuilder()

class PersonBuilder:
    
    def __init__(self):
        self.person = Person()
        
    def build(self):
        return self.person
    
    def works_as(self,job):
        self.person.position = job.upper()
        return self
    
    def known_as_with_firstname(self,first_name):
        self.person.first_name = first_name.capitalize()
        return self
    
    def known_as_with_last_name(self,last_name):
        self.person.last_name = last_name
        return self
    
    def born_in(self,dob):
        self.person.date_of_birth = dob
        return self
    
personA = Person.create()\
            .known_as_with_firstname("Souraj")\
                .known_as_with_last_name('Maity')\
                    .works_as("Scrum Master")\
                        .born_in("2 Feb 1996")\
                            .build()

personB = Person.create()\
            .known_as_with_firstname("William")\
                .known_as_with_last_name('Wesker')\
                    .works_as("Scientist")\
                        .born_in("Unknown")\
                            .build()
                    
print(personA)
print(personB)
    



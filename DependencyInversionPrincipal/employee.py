from abc import ABC, abstractmethod
from dataclasses import dataclass
import json

@dataclass
class Employee:
    id : int
    name : str
    age : int
    salary : float
    

class EmployeeRepo(ABC):
    
    @abstractmethod
    def find_all(self):
        pass
    
    @abstractmethod
    def find_by_id(self,id:int):
        pass
    
    @abstractmethod
    def save_emp(self,emp:Employee):
        pass
    
class EmployeeFileRepo(EmployeeRepo):
    
    def __init__(self,filename):
        
        self.filename = filename
        self.__emps = []
        
        
    def save_emp(self, emp: Employee):
        self.__emps.append(emp)
        with open(self.filename+'.json','w') as file:
            json_formatted = json.dumps(self.__emps ,default=lambda emp:emp.__dict__)
            file.write(json_formatted)
        return emp
    
    def find_all(self):
        with open(self.filename+'.json','r') as file:
            self.__emps = json.load(file, object_hook=lambda d: Employee(**d))
        return self.__emps
    
    def find_by_id(self, id: int):
        return filter(lambda x : x.id == id , self.__emps) 
    
class EmployeeInMemoryRepo(EmployeeRepo):
    
    def __init__(self) -> None:
        self.__employees = []
        
    def find_all(self):
        return self.__employees
    
    def save_emp(self, emp: Employee):
        self.__employees.append(emp)
        return emp
    
    
    def find_by_id(self, id: int):
        return list(filter(lambda emp : emp.id == id , self.__employees))
    
    
class EmployeeService:
    
    def __init__(self,repo:EmployeeRepo):
        self.repo = repo  
    
    def save(self,emp : Employee):
        saved = self.repo.save_emp(emp)
        return saved 

    def find_all(self):
        return self.repo.find_all()
    
    def find_by_id(self, id: int):
        return self.repo.find_by_id(id) 
    
    
        
emp_repo = EmployeeFileRepo('emp')
service = EmployeeService(emp_repo)     


mem_repo = EmployeeInMemoryRepo()
in_mem_serv = EmployeeService(mem_repo)     
        
print(service.save(Employee(1,"Sam",28,2000000)))
print(service.save(Employee(2,"Adam",28,2000000)))
print(service.save(Employee(3,"Eve",28,2000000)))
print(service.save(Employee(5,"Rhona",1,00)))

print(service.find_all())
    
    

print(in_mem_serv.save(Employee(1,"Ram",1,2000)))
print(in_mem_serv.save(Employee(2,"Adam",88,20)))
print(in_mem_serv.save(Employee(3,"Eve",8,200)))
print(in_mem_serv.save(Employee(5,"Rhona",18,11100)))
print(f'Filter Employee {in_mem_serv.find_by_id(3)}')

print(in_mem_serv.find_all())
        
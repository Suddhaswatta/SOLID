from abc import abstractmethod


class AbstractPrinter:
    
    @abstractmethod
    def print(self,document):
        pass

class AbstractScanner:
    
    @abstractmethod
    def scan(self,document):
        pass
    
class AbstractModernPrinter:
    
    @abstractmethod
    def print(self):
        pass
          
    @abstractmethod
    def scan(self):
        pass



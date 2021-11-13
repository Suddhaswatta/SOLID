"""
Single responsibility principle
separates primary concern from cross cutting concern.

Here in below example Journal is a primary concern 
while persisting object is a secondary concern

"""

class Journal:
    
    def __init__(self):
        self.entries = []
        self.pos = 0
        
    def add_entries(self,entry):
        self.entries.append(f'{self.pos+1} : {entry.strip()}')
        self.pos+=1
        return self
         
    def remove_entries(self,pos):
        del self.entries[pos]
        pos-=1
        
    def __str__(self):
        return "\n".join(self.entries)
    
class JournalRepo:
    
    @staticmethod
    def save_to_file(name,journal):
        file = open(name+".txt",mode="w")
        file.write(str(journal))
        file.close()
        

if __name__ == '__main__':
    
    journal = Journal()

    print(journal.add_entries("I eat "))
    print(journal.add_entries("I code "))
    print(journal.add_entries("I sleep "))
    repo = JournalRepo()
    repo.save_to_file("myFies",journal)





    
            
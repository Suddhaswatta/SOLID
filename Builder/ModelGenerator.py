class Field:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def __str__(self):
        return '%s : %s' % (self.name, self.type)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = ['from dataclasses import dataclass']
        lines.append('@dataclass')
        lines.append(f"class {self.name}:")
                     
        if not self.fields:
            lines.append('  pass')
        else:
            for f in self.fields:
                lines.append(f'\t{f}')
        return '\n'.join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()


code = CodeBuilder('Person')\
        .add_field('str','name')\
            .add_field('int','age')
        
file = open('file.py','w',encoding='utf-8')
file.write(str(code))
file.close()
    


      
    
    
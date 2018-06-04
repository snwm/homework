from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass
    
    
class Menu():
    commands = {}
    
    def __init__(self):
        self.limit = len(self.commands)
        self.index = 0
        
        
    def __next__(self):
        if self.index > self.limit:
            raise StopIteration
        self.index += 1
        return tuple(self.commands.items(self.index))
        
        
    def __iter__(self):
        return self
        
        
    def add_command(self, name, klass):
        if not name:
            raise CommandException('Command must have a name!')
        if not issubclass(klass, Command):
            raise CommandException('Class {} is not Command!'.format(klass))
            
        self.commands[name] = klass
        
       
    def execute(self, name, *args, **kwargs):
        if self.commands.get(name):
            req = self.commands.get(name)
            req(*args, **kwargs).execute()
        else:
            raise CommandException('Command with name "{}" not found'.format(name))
        
 
class CommandException(Exception):
    pass
    
    
class ShowCommand(Command):
    def __init__(self, task_id):
        pass
        
    def execute(self):
        pass
        

class ListCommand(Command):
    def __init__(self):
        pass
        
    def execute(self):
        pass
    
    


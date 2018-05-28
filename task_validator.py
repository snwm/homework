from abc import ABCMeta, abstractmethod

class Validator(metaclass=ABCMeta):
    types = {}
    
    @abstractmethod
    def validate(value):
        pass
        
        
    @classmethod   
    def get_instance(cls, name):
        return cls.types.get(name)
        
    
    @classmethod
    def add_type(cls, name, klass):
        if not issubclass(klass, Validator):
            raise ValidatorException(
                'Validator with name "{}" not found'.format(klass)
            )
            
        if not name:
            raise ValidatorException(
                'Validator must have a name!'
            )
            
        cls.types[name] = klass
    

class ValidatorException(Exception):
    pass
    
    
class EMailValidator(Validator):
    def validate(value):
        if not "@" in value or not "." in value:
            return False
            
        return True
    
    
class DateTimeValidator(Validator):

    def validate(value):
    
        def func_tpl(value, tpl):
            for i, v in enumerate(tpl):
                if v != "#" and value[i] != v:
                    return 0
            return 1
        
        templates = [
            "####-##-##",
            "####-##-#",
            "####-#-#",
            "####-##-## ##:##",
            "####-##-## ##:##:##",
            "#.#.####",
            "#.##.####",
            "##.##.####",
            "#.#.#### ##:##",
            "#.#.#### ##:##:##",
            "#/#/####",
            "#/##/####",
            "##/##/####",
            "#/#/#### ##:##",
            "#/#/#### ##:##:##"
        ]
        
        sum = 0
        for v in templates:
            sum += func_tpl(value, v)
        
        if sum is 0:
            return False
        
        return True
        
    
    
Validator.add_type("email", EMailValidator)
Validator.add_type("datetime", DateTimeValidator)

validator = Validator.get_instance('email')
print(validator.validate('info@itmo-it.org'))

validator = Validator.get_instance('datetime')
print(validator.validate('2017-09-01'))
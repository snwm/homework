from abc import ABCMeta, abstractmethod
import os
import pickle
import json

class ParamHandler(metaclass=ABCMeta):
    types = {}

    def __init__(self, source):
        self.source = source
        self.params = {}
        
    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
            
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
                'Class "{}" is not ParamHandler!'.format(klass)
            )

            
        cls.types[name] = klass
        
        
    def add_param(self, key, value):
        self.params[key] = value
        
        
    def get_all_params(self):
        return self.params
        
        
    @abstractmethod
    def read(self):
        pass
        
        
    @abstractmethod
    def write(self):
        pass
        
        
    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        
        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found!'.format(ext)
            )
            
        return klass(source, *args, **kwargs)
        
        
class ParamHandlerException(Exception):
    def __init__(self, value):
        ParamHandlerException.txt = value
        
        
class JsonParamHandler(ParamHandler):
    def read(self):
        with open(self.source) as f:
            readed_data = json.load(f)
            return '{}'.format(readed_data)
        
        
    def write(self):
        with open(self.source, 'w') as f:
            json.dump(self.params, f, indent=4)
            
            
class PickleParamHandler(ParamHandler):
    def read(self):
        with open(self.source, 'rb') as f:
            readed_data = pickle.load(f)
            return '{}'.format(readed_data)
        
        
    def write(self):
        with open(self.source, 'wb') as f:
            pickle.dump(self.params, f)
        

ParamHandler.add_type('json', JsonParamHandler)
ParamHandler.add_type('pickle', PickleParamHandler)

config = ParamHandler.get_instance('./test1.json')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write() # запись файла в XML формате
print(config.read())

config = ParamHandler.get_instance('./test2.pickle')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write() # запись файла в XML формате
print(config.read())
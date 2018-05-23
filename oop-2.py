from abc import ABCMeta, abstractmethod

class TrainingHandler(metaclass=ABCMeta):
    __instance = None
    params = {}

       
    def add_param(self, klass, value):
        return klass(value, klass.add_param)
        
        
    def remove_param(self):
        pass

        
    def show_obj(self):
        pass
        
        
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
        
        
class CourseTrainingHandler(TrainingHandler):
    def __init__(self, value, func):
        self.cuorsevalue = value
        self.func = func
        return self.func(self)
        
    def add_param(self):
        if not self.params.get("courses"):
            self.params["courses"] = {}
        self.params["courses"][self.cuorsevalue] = {}
        print(self.params)
        
        
traning = TrainingHandler.get_instance()
traning.add_param(CourseTrainingHandler, "kurs1")
traning.add_param(CourseTrainingHandler, "kurs2")
traning.add_param(CourseTrainingHandler, "kurs3")

'''
Что-то пока подзастрял. Идея была такая: все будут добавляться/удаляться через универсальные методы add_param/remove_param . В качестве аргументов передаются название класса, и данные. В этих классах идет обработка принятых данных, далее распределение по нужным местам
Возможно совершенно неправильным путем пошел.
'''
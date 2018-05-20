class ConfogMain(object):
    __instance = None # статическое св-во

    def __init__(self):
        self.__params = {}

    @classmethod # статический метод
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def add_param(self, key, value):
        self.__params[key] = value

    def get_param(self, key):
        return self.__params.get(key)

    def remove_param(self, key):
        if key in self.__params:
            del self.__params[key]

    def save_to_file(file, data):
        """Запись данных в файл"""
        
    def load_from_file(file):
        """Чтение данных из файла"""

#Класс формата 1, наследует общий класс ConfogMain
class Format1Config(ConfogMain):
    def __init__(self):
        super().__init__()
        
    def save(self, file, data):
        """Обработка и сохранение данных в нужный формат"""
        save_to_file(file, data)
        
    def load(self, file):
        var = load_from_file(file)
        """чтение и обработка файла в нашем формате"""
        
#Класс формата 2, наследует общий класс ConfogMain
class Format2Config(ConfogMain):
    def __init__(self):
        super().__init__()
        
    def save(self, file, data):
        """Обработка и сохранение данных в нужный формат"""
        save_to_file(file, data)
        
    def load(self, file):
        var = load_from_file(file)
        """чтение и обработка файла в нашем формате"""
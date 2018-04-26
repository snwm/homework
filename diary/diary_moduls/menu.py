def run():
    print(print_menu())
    try:
        print("Введите число: ")
        choice = int(input())
        if(choice == 6): return
        start_func(choice)
        run()
    except ValueError:
        return print_error('Не корректное число!')
    except KeyError:
        return print_error('Такого пункта нет!')
	
def print_menu():
    menu = '''
Ежедневник. Выберите действие:

1: Вывести список задач
2: Добавить задачу
3: Отредактировать задачу
4: Завершить задачу
5: Начать задачу сначала
6: Выход
	'''
    return menu

def start_func(f):
    functions = {
        1: print_task,
        2: add_task,
        3: edit_task,
        4: end_task,
        5: again_task,
        6: exit_task,
	}
	
    return functions[f]()

def print_task():
    print("Вывести список задач")
	
def add_task():
    print("Добавить задачу")
	
def edit_task():
    print("Отредактировать задачу")
	
def end_task():
    print("Завершить задачу")
	
def again_task():
    print("Начать задачу сначала")
	
def exit_task():
    print("Начать задачу сначала")
	
def print_error(b):
    print(b)
    run()
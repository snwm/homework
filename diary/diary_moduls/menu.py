import sys
from diary_moduls import req_db

get_connection = lambda: req_db.connect('db.sqlite')
	
    
def print_menu():
    menu = '''
Ежедневник. Выберите действие:

1: Вывести список задач
 1.1: Вывести только Не выполненные
 1.2: Вывести только Выполненные
2: Добавить задачу
3: Отредактировать задачу
4: Завершить задачу
5: Начать задачу сначала
6: Поиск задачи по содержимому в названии
 6.1: Поиск по содержимому в тексте
q: Выход
	'''
    return menu

    
def start_func(f):
    functions = {
        '1': print_task,
        '2': add_task,
        '3': edit_task,
        '4': end_task,
        '5': again_task,
        '6': search_task,
        'q': exit_task,
	}
    
    sub_function = {
        '1.1':print_task,
        '1.2':print_task,
        '6.1':search_task
    }
    
    action = functions.get(f)
    sub_action = sub_function.get(f)
    
    if action:
        return action()
    elif sub_action:
        return sub_action(f)
    else:
        print('\nНе известная команда')

            
def print_task(num=0):
    with get_connection() as conn:
        print('\n'+req_db.list_tasks(conn, num))
	
    
def add_task():
    name = input('\nВведите название задачи: ')
    text = input('\nВведите текст задачи: ')
    time = input('\nВведите запланированное время: ')
    
    with get_connection() as conn:
        req_db.add_task(conn, name, text, time)
        
    print(print_menu())
	
    
def edit_task():
    num_task = input('\nВведите номер задачи: ')
    with get_connection() as conn:
        result_edit_menu = req_db.menu_edit(conn, num_task)
        
        if not result_edit_menu:
            return print("\nВ базе такой задачи не найдено")
            
        print(result_edit_menu)
    
    num_edit = input("\nВыберите, что хотите поменять: ")
    edit_text = input("\nВведите новые данные: ")
    
    with get_connection() as conn:
        req_db.update_task(conn, num_edit, edit_text, num_task)
        
    print(print_menu())
    
    
def end_task(choice=0):
    num_task = input('\nВведите номер задачи: ')
    with get_connection() as conn:
        if not req_db.menu_edit(conn, num_task):
            return print("\nТакой задачи в базе не найдено")
            
        req_db.end_task(conn, num_task, choice)
        
    print(print_menu())
	
    
def again_task():
    end_task(1)
    
    
def search_task(choice=0):
    text_search = input('\nВведите фразу для поиска: ')
    with get_connection() as conn:
        print('\n'+req_db.search_task(conn, choice, text_search))
	
    
def exit_task():
    sys.exit(0)
	
    
def run():
    with get_connection() as conn:
        req_db.initialize(conn)
        
    print(print_menu())
    
    while 1:
        choice = input('\nВведите команду: ')
        start_func(choice)
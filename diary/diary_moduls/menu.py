import sys
from diary_moduls import req_db, convert_date

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
 6.2: Поиск по интервалу дат
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
        '6.2':search_task_by_date,
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
	
    
def valid_input(inp):
    enter_text = input(inp)
    while not enter_text:
        enter_text = input(inp)
            
    return enter_text
    
    
def valid_date(inp, format="%d.%m.%Y %H:%M"):
    enter_date = convert_date.check_date(input(inp), format)
    while not enter_date:
        enter_date = convert_date.check_date(input("\nОшибка формата даты"+inp), format)
        
    return enter_date
    
    
def add_task():
    name = valid_input("\nВведите название задачи: ")
    text = valid_input("\nВведите текст задачи: ")
    time = valid_date("\nВведите запланированную дату и время (например 01.01.2018 01:08): ")
    time = convert_date.convert_to_unix_format(time)
        
    with get_connection() as conn:
        req_db.add_task(conn, name, text, time)
        
    print(print_menu())
	
    
def edit_task():
    num_task = valid_input('\nВведите номер задачи: ')
    with get_connection() as conn:
        result_edit_menu = req_db.menu_edit(conn, num_task)
        
        while not result_edit_menu:
            num_task = valid_input('\nТакой задачи нет в базе\nВведите номер задачи: ')
            result_edit_menu = req_db.menu_edit(conn, num_task)
            
        print(result_edit_menu)
    
    num_edit = valid_input("\nВыберите, что хотите поменять: ")
    
    while not req_db.colums_db(num_edit):
        num_edit = valid_input("\nВы выбрали несуществующие даннные\nВыберите, что хотите поменять: ")
    
    if(num_edit == "3"):
        edit_text = valid_date("\nВведите новую дату (например 01.01.2018 01:08): ")
        edit_text = convert_date.convert_to_unix_format(edit_text)
    else:
        edit_text = valid_input("\nВведите новые данные: ")
    
    with get_connection() as conn:
        req_db.update_task(conn, num_edit, edit_text, num_task)
        
    print(print_menu())
    
    
def end_task(choice=0):
    num_task = valid_input('\nВведите номер задачи: ')
    with get_connection() as conn:
        while not req_db.menu_edit(conn, num_task):
            num_task = valid_input("\nТакой задачи в базе не найдено\nВведите номер задачи: ")
            
        req_db.end_task(conn, num_task, choice)
        
    print(print_menu())
	
    
def again_task():
    end_task(1)
    
    
def search_task(choice=0):
    text_search = valid_input('\nВведите фразу для поиска: ')
    with get_connection() as conn:
        print('\n'+req_db.search_task(conn, choice, text_search))
	
def search_task_by_date():
    date_start = valid_date("\nВведите начальную дату (например 01.01.2018): ", "%d.%m.%Y")
    date_start = convert_date.convert_to_unix_format(date_start, '%d.%m.%Y')
    date_over = valid_date("\nВведите конечную дату (например 01.01.2018): ", "%d.%m.%Y")
    date_over = convert_date.convert_to_unix_format(date_over, '%d.%m.%Y')
    with get_connection() as conn:
        print('\n'+req_db.search_task_by_date(conn, date_start, date_over))
    
    
def exit_task():
    sys.exit(0)
	
    
def run():
    with get_connection() as conn:
        req_db.initialize(conn)
        
    print(print_menu())
    
    while 1:
        choice = valid_input('\nВведите команду: ')
        start_func(choice)
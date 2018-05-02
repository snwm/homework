import os.path as Path
import sqlite3

SQL_INSERT_TASK = 'INSERT INTO diary (name, text, deadline, status) VALUES (?, ?, ?, ?)'
SQL_SELECT_ALL = '''
    SELECT
        id, name, text, deadline, status
    FROM
        diary
    '''
SQL_SELECT_TASK_BY_ID = SQL_SELECT_ALL + ' WHERE id=?'
SQL_SELECT_TASK_BY_STATUS = SQL_SELECT_ALL + ' WHERE status LIKE ? ORDER BY id DESC'


def sql_search(column):
    sql = '''
    WHERE '''+column+''' LIKE ? ORDER BY id DESC
    '''
    return sql
    

def sql_update_task(b):
    sql = '''
    UPDATE diary SET '''+b+'''=? WHERE id=?
    '''
    return sql

    
def connect(db_name=None):
    """Выполняет подключение к БД"""
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)

    return conn


def initialize(conn):
    """Инициализирует структуру БД."""
    script_path = Path.join(Path.dirname(__file__), 'schema.sql')

    with conn, open(script_path) as f:
        conn.executescript(f.read())


def add_task(conn, name, text, time):
    conn.execute(SQL_INSERT_TASK, (name, text, time, "Не выполнено"))
    

def output_list_tasks(result):
    show_result = "";
    for i, value in enumerate(result):
        show_result += '{} | {} | {} | {} | {}'.format(value[0], value[1], value[2], value[3], value[4]) + '\n'
    
    if not show_result: 
        return "Такой задачи в базе не найдено"
        
    return show_result

    
def list_tasks(conn, num):
    status = {0:'%', '1.1':'Не выполнено', '1.2': 'Выполнено'}
    cursor = conn.execute(SQL_SELECT_TASK_BY_STATUS, (status.get(num), ))
    result = cursor.fetchall()
    
    return output_list_tasks(result)
    
    
def menu_edit(conn, id):
    cursor = conn.execute(SQL_SELECT_TASK_BY_ID, (id,))
    result = cursor.fetchone()
    
    if not result:
        return
    
    show_result = '''
1. '''+ result[1] +'''
2. '''+ result[2] + '''
3. '''+ result[3] + '''
    '''
    
    return show_result
    
    
def colums_db(a):
    columns = {
        '1': 'name',
        '2': 'text',
        '3': 'deadline'
    }
    
    return columns.get(a)
    

def update_task(conn, num_column, new_data, id):
    if not colums_db(num_column):
        return print("\n !!!!Вы выбрали несуществующие даннные!!!!")
    conn.execute(sql_update_task(colums_db(num_column)), (new_data, id))
    

def end_task(conn, id_task, choice):
    end_start_task = {0:"Выполнено", 1:"Не выполнено"}
    conn.execute(sql_update_task("status"), (end_start_task.get(choice), id_task))
    
   
def search_task(conn, choice, search_text):
    name_column = {0:'name', '6.1':'text'}
    cursor = conn.execute(SQL_SELECT_ALL+sql_search(name_column.get(choice)), ('%'+search_text+'%', ))
    result = cursor.fetchall()
    
    return output_list_tasks(result)
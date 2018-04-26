﻿import sqlite3

def creat():
    with sqlite3.connect('db.sqlite') as conn:
        sql = '''
            CREATE TABLE IF NOT EXISTS `diary` (
            `id`	INTEGER PRIMARY KEY AUTOINCREMENT,
            `name`	TEXT NOT NULL,
            `text`	TEXT NOT NULL,
            `deadline`	TEXT NOT NULL,
            `status`	TEXT NOT NULL DEFAULT 'Не выполнено'
        );
        '''
        cursor = conn.execute(sql)
    
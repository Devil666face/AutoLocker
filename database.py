import sqlite3

def unlock_state():
    with sqlite3.connect('database.db') as DB:
        select_query = f"SELECT unlock FROM control;"
        for state in do_query(select_query,DB):
            return convert_int_to_bool(state[0])

def screen_state():
    with sqlite3.connect('database.db') as DB:
        select_query = f"SELECT screen FROM control;"
        for state in do_query(select_query,DB):
            return convert_int_to_bool(state[0])

def detect_state():
    with sqlite3.connect('database.db') as DB:
        select_query = f"SELECT detect FROM control;"
        for state in do_query(select_query,DB):
            return convert_int_to_bool(state[0])

def update_unlock_state(state):
    with sqlite3.connect('database.db') as DB:
        update_query = ''
        if state:
            update_query = f"UPDATE control SET unlock = 1;"
        else:
            update_query = f"UPDATE control SET unlock = 0;"
        do_query(update_query,DB)

def update_screen_state(state):
    with sqlite3.connect('database.db') as DB:
        update_query = ''
        if state:
            update_query = f"UPDATE control SET screen = 1;"
        else:
            update_query = f"UPDATE control SET screen = 0;"
        do_query(update_query,DB)

def update_detect_state(state):
    with sqlite3.connect('database.db') as DB:
        update_query = ''
        if state:
            update_query = f"UPDATE control SET detect = 1;"
        else:
            update_query = f"UPDATE control SET detect = 0;"
        do_query(update_query,DB)

def do_query(sql_query,DB):
    cursor = DB.cursor()
    cursor.execute(sql_query)
    DB.commit()
    return cursor

def convert_int_to_bool(number):
    if number==1:
        return True
    else:
        return False

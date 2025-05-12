import sqlite3
from datetime import datetime, timedelta

def create_table() -> None:
    with sqlite3.connect("insert custom path") as connection:
        cursor = connection.cursor()
        
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        description TEXT
        );
        '''

        cursor.execute(create_table_query)
        connection.commit()
        print("Succesfully created Events database")

#---------------------------------------------------------------------------

def flush_table() -> None:
    with sqlite3.connect("insert custom path") as connection:
        cursor = connection.cursor()
        query ='''
        DELETE FROM Events;
        '''
        query2 = '''
        DELETE FROM sqlite_sequence WHERE name='Events';
        '''
        cursor.execute(query)
        cursor.execute(query2)
        connection.commit()

#---------------------------------------------------------------------------

def add_event(name: str, date: str, end_date: str, info: str) -> None:
    with sqlite3.connect('insert custom path') as connection:
        cursor = connection.cursor()

        insert_query = '''
        INSERT INTO Events (name, date, end_date, description)
        VALUES (?, ?, ?, ?);
        '''

        event_data = (f'{name}', f'{date+":00"}', f'{end_date+":00"}', f'{info}')
        cursor.execute(insert_query, event_data)
        connection.commit()

#---------------------------------------------------------------------------

def remove_event(id: int) -> None:
    with sqlite3.connect('insert custom path') as connection:
        cursor = connection.cursor()
        
        remove_query = f'''
        DELETE FROM Events
        WHERE id = {id};
        '''

        cursor.execute(remove_query)
        connection.commit()

#---------------------------------------------------------------------------

def get_all() -> tuple:
   with sqlite3.connect('insert custom path') as connection:
        cursor = connection.cursor() 

        pull_query = '''
        SELECT * FROM Events ORDER BY date;
        '''

        cursor.execute(pull_query)
        all_events = cursor.fetchall()

        return all_events

#---------------------------------------------------------------------------

def get_next_ndays(n_days: int) -> tuple:
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d ') + "00:00"

    if n_days == 0:
        future = now_str[:-5]
        future_str = future + "23:59"
    else:
        future = now + timedelta(days=n_days)
        future_str = future.strftime('%Y-%m-%d %H:%M')

    with sqlite3.connect('insert custom path') as connection:
        cursor = connection.cursor()
 
        query = f'''
        SELECT * FROM Events WHERE date BETWEEN ? AND ? ORDER BY date;
        '''
        cursor.execute(query, (now_str, future_str))

        events = cursor.fetchall()

        return events

#---------------------------------------------------------------------------

def get_index() -> list:
    with sqlite3.connect('insert custom path') as connection:
        cursor = connection.cursor()

        query = '''
        SELECT rowid FROM Events ORDER BY rowid;
        '''
 
        cursor.execute(query)
        indexes = [row[0] for row in cursor.fetchall()]

        return indexes

#---------------------------------------------------------------------------

def get_day(day: str, end_day: str) -> tuple:

    with sqlite3.connect('insert custom path') as connection:
        cursor = connection.cursor()

        query = '''
        SELECT * FROM Events WHERE date BETWEEN ? and ? ORDER BY date;
        '''
 
        cursor.execute(query, (day, end_day))
        events = cursor.fetchall()

        return events


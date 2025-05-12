import sqlite3
from datetime import datetime
from backend import (
                    add_event,
                    flush_table,
                    remove_event,
                    get_all,
                    get_next_ndays,
                    get_index,
                    get_day
                    )
from functions import (valid_date)

now = datetime.now()
now_str = now.strftime('%Y-%m-%d ')

#---------------------------------------------------------------------------

def display_all(events: list) -> None:
    identificador = 'id'.ljust(6, " ")
    name = 'Evento'.ljust(20, " ")
    date = 'Fecha'.ljust(25, " ")
    end = 'Termino'.ljust(25, " ")
    descr = 'Info'.ljust(30, " ")

    print(identificador + name + date + end + descr)
    for event in events:
        event_id = str(event[0]).ljust(6, " ")
        event_name = str(event[1]).ljust(20, " ")
        event_start = str(event[2])[:-3].ljust(25, " ")
        event_end = str(event[3])[:-3].ljust(25, " ")
        event_descr = str(event[4]).ljust(30, " ")

        print(event_id + event_name + event_start + event_end + event_descr)

    print("")

#---------------------------------------------------------------------------

def menu() -> str:
    print(f'Current: {now_str}')
    print("[1] Show day")
    print("[2] Show week")
    print("[3] Show month")
    print("[4] Show all")
    print("[5] Look day")
    print("[a/r] Add/Remove event")
    print("[q] Quit")
    print("-" * 60)

    usr_input = input("Input: ")

    if usr_input in ["1", "2", "3", "4", "5", "a", "r", "q"]:
        return usr_input
    else:
        print("")
        print("Invalid")
        print("")

#---------------------------------------------------------------------------

def auto_complete(date: str, end_date: str) -> str:
    if (len(date) == 1 and date.isdigit()) or (len(date) == 7):
        date = "0" + date

    if (len(end_date) == 1 and end_date.isdigit()) or (len(end_date) == 7):
        end_date = "0" + end_date

    # SHORT FORMAT + NO HOUR
    if len(date) == 2 and date.isdigit() and end_date == "":
        current_date = datetime.now()
        current_str = current_date.strftime("%Y-%m")
        end_date = current_str + "-" + date + " 23:59"
        date = current_str + "-" + date + " 00:00"

    if len(date) == 8 and len(end_date) == 8:
        current_date = datetime.now()
        current_str = current_date.strftime("%Y-%m")
        date = current_str + "-" + date
        end_date = current_str + "-" + end_date

    if len(date) == 10 and valid_date(date) and end_date == "":
        end_date = date + " 23:59"
        date = date + " 00:00"

    return (date, end_date)

#---------------------------------------------------------------------------

def usr_add() -> None:
    """
    Function allows to enter activies to be done during day by
    just giving a date and no end_date
    """
    name = input("Name: ")
    date = input("Date: ")
    end_date = input("End date: ")
    info = input("Info: ")

    date, end_date = auto_complete(date, end_date)
 
    if valid_date(date) and valid_date(end_date):
        add_event(name, date, end_date, info)

    else:
        print("")
        print("Invalid date format")
        print("")

#---------------------------------------------------------------------------

def usr_del() -> None:
    id_input = input("Event id: ")
    try:
        int(id_input)
    except ValuError:
        print("")
        print("Invalid id")
        print("")
    else:
        if int(id_input) in get_index():
            remove_event(int(id_input))
        else:
            print("")
            print("Invalid id")
            print("")

#---------------------------------------------------------------------------

def specific_day() -> None:
    day = input("Day: ")
    day, end_day = auto_complete(day, "")
    if valid_date(day):
        return get_day(day, end_day)
    else:
        print("")
        print("Invalid format")
        print("")

#---------------------------------------------------------------------------

def main() -> None:
    run = True

    while run:
        request = menu()
        if request == "1":
            display_all(get_next_ndays(0))
        elif request == "2":
            display_all(get_next_ndays(7))
        elif request == "3":
            display_all(get_next_ndays(31))
        elif request == "4":
            display_all(get_all())
        elif request == "5":
            display_all(specific_day())
        elif request == "a":
            usr_add()
        elif request == "r":
            usr_del()
        elif request == "q":
            run = False
            break

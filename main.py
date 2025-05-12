import sqlite3
from backend import (
                    add_event,
                    flush_table,
                    remove_event,
                    get_all,
                    get_index,
                    create_table,
                    )
from front import (
                    main,
                    display_all,
                    get_next_ndays
                    )
import os
import sys

#flush_table()
if not os.path.isfile('insert custom path'):
    create_table()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "auto":
            display_all(get_next_ndays(0))
    else:
        main()

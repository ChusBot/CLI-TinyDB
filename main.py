from os import path, pardir
from pathlib import Path
from tinydb import TinyDB

if __name__ == '__main__':
    pwd = Path('.').absolute()
    print(pwd)

    command = ''
    db_name = 'db.json'
    table_name = None
    while command != '/q':
        command = input('>> ')

        if command == "??":
            print("/c {file} - select db. file=db.json by default")
            print("/? - print info")
            print("/l - print tables list")
            print("/t {table} - select table")
            print("\n/q - exit")

        if command.startswith('/c'):
            db_name = command[3:].strip()
            command = '/?'

        if command.startswith('/?'):
            print(f'db={db_name}')
            if table_name is not None:
                print(f'table={table_name}')

        if command.startswith('/l'):
            with TinyDB(db_name) as db:
                for t in db.tables():
                    print(t)

        if command.startswith('/t'):
            table_name = command[3:].strip()

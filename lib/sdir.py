
import sqlite3
from os import getcwd, path, chdir
from shutil import which

import datetime
import pyperclip
from tabulate import tabulate
import random


now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
executable_path = path.dirname(which("sdir.exe"))


def DB():
    conn = sqlite3.connect(f"{executable_path}\\sdir.db.sqlite3")
    return conn


def __create_table(conn):
    c = conn.cursor()
    c.execute('''
        CREATE TABLE if not exists Directory (
            id INTEGER PRIMARY KEY,
            date DATETIME,
            label TEXT,
            directory TEXT
        )
    ''')
    conn.commit()


def __insert_directory(conn, label):
    c = conn.cursor()
    random_id = random.randint(10000, 99999)
    c.execute("INSERT INTO Directory(id, date, label, directory) VALUES(?,?,?,?)",
              (random_id, now, label, getcwd()))
    conn.commit()


def __del_directory(conn, id):
    c = conn.cursor()
    c.execute("DELETE FROM Directory WHERE id=?", (id,))
    conn.commit()


def __del_directory_all(conn):
    c = conn.cursor()
    c.execute("DELETE FROM Directory")
    conn.commit()


def __select_dir_all(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM Directory")
    result = c.fetchall()

    if not result:
        print("empty.")
        return

    headers = ["ID", "Date", "Label", "Directory Path"]
    data = [(str(row[0]), str(row[1]), row[2], row[3]) for row in result]
    print(tabulate(data, headers=headers, tablefmt="plain"))
    conn.commit()


def create_table_once(db):
    __create_table(db)


def save_dir(db, label):
    __insert_directory(db, label)


def remove_dir(db, id):
    __del_directory(db, id)


def remove_dir_all(db):
    __del_directory_all(db)


def list_dir(db):
    __select_dir_all(db)


def get_directory_by_id(db, id):
    c = db.cursor()
    c.execute("SELECT directory FROM Directory WHERE id=?", (id,))
    result = c.fetchone()
    return result


def ch_dir(db, id):
    try:
        directory = get_directory_by_id(db, id)
        chdir(directory[0])
    except Exception as e:
        print(e)


def copy_path_to_clip(db, id):
    directory = get_directory_by_id(db, id)
    if directory is not None:
        path = directory[0]
        pyperclip.copy(path)
        print("Path copied to clipboard:", path)
    else:
        print("Directory not found with ID:", id)

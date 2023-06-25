import sqlite3
from os import getcwd,chdir,path
from shutil import which
import datetime
import pyperclip



now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
executable_path = path.dirname(which("sdir.exe"))

def DB():
	conn = sqlite3.connect(f"{executable_path}\\sdir.db.sqlite3")
	# conn = sqlite3.connect("sdir.db.sqlite3")
	return conn

def __create_table(conn):
	c = conn.cursor()
	c.execute('''
		CREATE TABLE if not exists Directory (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			date DATETIME,
			directory TEXT
		)
	''')
	conn.commit()




def __insert_directory(conn):
	c = conn.cursor()
	c.execute("INSERT INTO Directory(date,directory) VALUES(?,?)",(now,getcwd(),))
	conn.commit()





def __del_directory(conn,id):
	c = conn.cursor()
	c.execute("DELETE FROM Directory WHERE id=?",(id,))
	conn.commit()




def __del_directory_all(conn):
	c = conn.cursor()
	c.execute("DELETE FROM Directory")
	conn.commit()




def __select_dir_all(conn):
	c = conn.cursor()
	c.execute("SELECT * FROM Directory")
	result = c.fetchall()
	print(f'{str("ID").ljust(5)}  {str("Date").ljust(20)}  Directory Path')

	if result == []:
		print("empty.")
		return

	for row in result:
		print(f'{str(row[0]).ljust(5)}| {str(row[1]).ljust(5)}| {row[2]}')

	conn.commit()


def create_table_once(db):
	__create_table(db)


def save_dir(db):
	__insert_directory(db)

def remove_dir(db,id):
	__del_directory(db,id)


def remove_dir_all(db):
	__del_directory_all(db)

def list_dir(db):
	__select_dir_all(db)

def get_directory_by_id(db, id):
		c = db.cursor()
		c.execute("SELECT directory FROM Directory WHERE id=?", (id,))
		result = c.fetchone()
		return result


def copy_path_to_clip(db, id):
    directory = get_directory_by_id(db, id)
    if directory is not None:
        path = directory[0]
        pyperclip.copy(path)
        print("Path copied to clipboard:", path)
    else:
        print("Directory not found with ID:", id)

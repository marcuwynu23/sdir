import sys
from src.sdir import *
help = "use these flags: -s,-r,-ra,-l"
def main():
	db = DB()
	args = sys.argv
	create_table_once(db)
	try:
		cmd = args[1]

		if cmd == "-s":
			save_dir(db)

		elif cmd == "-r":
			id = args[2]
			remove_dir(db,id)

		elif cmd == "-ra":
			remove_dir_all(db)

		elif cmd == "-l":
			list_dir(db)
		else:
			print(help)

	except IndexError as err:
		print(help)

if __name__ == '__main__':
	main()

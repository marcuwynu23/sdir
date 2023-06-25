from lib.sdir import *
import fire
from tabulate import tabulate


def main(cmd=None, id=None):
    db = DB()
    create_table_once(db)
    
    if cmd == "save":
        save_dir(db)
    elif cmd == "remove" and id is not None:
        remove_dir(db, id)
    elif cmd == "remove-all":
        remove_dir_all(db)
    elif cmd == "list":
        list_dir(db)
    elif cmd == "clip" and id is not None:
        copy_path_to_clip(db, id)
    else:
        help_table = [
            ["Command", "Description"],
            ["save", "Save the current directory."],
            ["remove [id]", "Remove a saved directory by its ID."],
            ["remove-all", "Remove all saved directories."],
            ["list", "List all saved directories."],
            ["clip [id]", "Copy the path of a saved directory to the clipboard."]
        ]
        print("SDIR - Saved Directory")
        print(tabulate(help_table, headers="firstrow", tablefmt="plain"))
        print("\nAuthor: Mark Wayne Menorca")
        print("GitHub: https://github.com/marcuwynu23/sdir")


if __name__ == '__main__':
    fire.Fire(main)

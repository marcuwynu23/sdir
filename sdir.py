from lib.sdir import *
import fire
from tabulate import tabulate


class SDir:
    def __init__(self):
        self.__db = DB()
        create_table_once(self.__db)

    def save(self, label):
        """Save the current directory."""
        save_dir(self.__db, label)

    def remove(self, id):
        """Remove a saved directory by its ID.

        Args:
            id (int): The ID of the directory to remove.
        """
        remove_dir(self.__db, id)

    def remove_all(self):
        """Remove all saved directories."""
        remove_dir_all(self.__db)

    def list(self):
        """List all saved directories."""
        list_dir(self.__db)

    def clip(self, id):
        """Copy the path of a saved directory to the clipboard.

        Args:
            id (int): The ID of the directory to copy the path from.
        """
        copy_path_to_clip(self.__db, id)

    def help(self):
        """Display the help information for all commands."""
        help_table = [
            ["Command", "Description"],
            ["save [label]", "Save the current directory."],
            ["remove [id]", "Remove a saved directory by its ID."],
            ["remove-all", "Remove all saved directories."],
            ["list", "List all saved directories."],
            ["clip [id]", "Copy the path of a saved directory to the clipboard."]
        ]
        print("SDIR v1.0.0")
        print("Author: Mark Wayne Menorca")
        print("GitHub: https://github.com/marcuwynu23/sdir")
        print("Description: SDIR is a tool to save and manage directories\n")
        print(tabulate(help_table, headers="firstrow", tablefmt="plain"))


def main():
    sdir = SDir()
    fire.Fire(sdir, name="sdir")


if __name__ == '__main__':
    main()

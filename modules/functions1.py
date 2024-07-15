# list constants at the top of the file, easy to change it once instead of everywhere
FILEPATH = "text_files/todo_list1.txt"

def get_todos(filepath=FILEPATH):

    """ Read a text file and return the list of to-do items."""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):

    """ Write the to-do items list in the text file."""

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# only prints if we're running this specific function, doesn't if we run it somewhere else
# use it to test a specific file without running all the files
if __name__ == "__main__":
    print("hello from functions file")

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list
    of to-do item
    """
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


freezing_point = 0
boiling_point = 0


def count(phrase):
    return phrase.count('.')
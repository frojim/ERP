""" Common module
implement commonly used functions here
"""

import random
import ui
import data_manager
import string


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    generated = ""
    id = []
    specials = ["#", "&", "@", "?", "!", "*", "/"]
    for i in range(2):
        i = ''.join(random.choice(string.ascii_lowercase))
        id.append(i)

    for i in range(2):
        i = ''.join(random.choice(string.ascii_uppercase))
        id.append(i)

    for i in range(2):
        i = ''.join(random.choice(string.digits))
        id.append(i)

    for i in range(2):
        i = ''.join(random.choice(specials))
        id.append(i)

    random.shuffle(id)

    generated = ("".join(str(item) for item in id))

    return generated


def show_table(table, title_list):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    ui.print_table(table, title_list)

def add(table, questions_asked):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    new_record = ui.get_inputs(questions_asked, " ")
    new_record.insert(0, generate_random(table))
    table.append(new_record)
    print(table)
    return table


def remove(table, unique_id, title_list):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    ui.print_table(table, title_list)
    print('')
    unique_id = input("ID of record to remove: ")
    for line in table:
        if unique_id in line:
            table.remove(line)
    print(table)
    return table


def update(table, unique_id, title_list):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    ui.print_table(table, title_list)
    row_to_change = []
    user_choice = input("ID of record to change: ")
    for row in table:
        if user_choice in row:
            row_to_change.append(row)
    row_to_change = row_to_change[0]
    print(row_to_change)
    table.remove(row_to_change)
    element_to_change = int(input("Number of element to change: "))
    changed_element = str(input("Change element to: "))
    element_to_change = element_to_change - 1
    print(element_to_change)
    row_to_change[element_to_change] = changed_element
    table.append(row_to_change)
    print(table)
    
    return table
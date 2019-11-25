""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    while True:
        
        title = "Inventory module"
        exit_message = "Exit to main"
        options = ["Show table",
                    "Add item",
                    "Remove item",
                    "Update item",
                    "Available items",
                    "Avg durability by manufacturer"]
        ui.print_menu(title, options, exit_message)

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        file_name = "/home/frojim/Documents/CC/lightweight-erp-python-extremely-random-programmers/inventory/inventory.csv"
        table = data_manager.get_table_from_file(file_name)
        title_list = ['id', 'title', 'manufacturer', 'purchase_year', 'durability']
        questions_asked = ['title: ', 'manufacturer: ', 'purchase_year: ', 'durability: ']
        unique_id = ''

        if option == "1":
            common.show_table(table, title_list)
        elif option == "2":
            common.add(table, questions_asked)
        elif option == "3":
            common.remove(table, unique_id, title_list)
        elif option == "4":
            common.update(table, unique_id, title_list)
        elif option == "5":
            get_available_items(table, year)
        elif option == "6":
            get_average_durability_by_manufacturers(table)
        elif option == "0":
            break




    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code

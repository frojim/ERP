""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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

    # you code

    while True:
        
        title = "Accounting module"
        exit_message = "Exit to main"
        options = ["Show table",
                    "Add item",
                    "Remove item",
                    "Update item",
                    "Highest profit year",
                    "Avg profit by item"]
        ui.print_menu(title, options, exit_message)

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        file_name = "/home/frojim/Documents/CC/lightweight-erp-python-extremely-random-programmers/accounting/items.csv"
        table = data_manager.get_table_from_file(file_name)
        title_list = ['id', 'month', 'day', 'year', 'type', 'amount']
        questions_asked = ['month: ', 'day: ', 'year: ', 'type: ', 'amount: ']
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
            which_year_max(table)
        elif option == "6":
            avg_amount(table, year)
        elif option == "0":
            break




def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code

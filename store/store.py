""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
    while True:
        
        title = "Store module"
        exit_message = "Exit to main"
        options = ["Show table",
                    "Add item",
                    "Remove item",
                    "Update item",
                    "Games by manufacturers",
                    "Avg stock by manufacturer"]
        ui.print_menu(title, options, exit_message)

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        file_name = "/home/frojim/Documents/CC/lightweight-erp-python-extremely-random-programmers/store/games.csv"
        table = data_manager.get_table_from_file(file_name)
        title_list = ['id', 'title', 'manufacturer', 'price', 'in_stock']
        questions_asked = ['title: ', 'manufacturer: ', 'price: ', 'in_stock: ']
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
            get_average_by_manufacturer(table, manufacturer)
        elif option == "6":
            get_counts_by_manufacturers(table)
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
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code

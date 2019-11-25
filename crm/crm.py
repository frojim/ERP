""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
        
        title = "Customer Relationship Management module"
        exit_message = "Exit to main"
        options = ["Show table",
                    "Add item",
                    "Remove item",
                    "Update item",
                    "Longest name",
                    "Subscription"]
        ui.print_menu(title, options, exit_message)

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        file_name = "/home/frojim/Documents/CC/lightweight-erp-python-extremely-random-programmers/crm/customers.csv"
        table = data_manager.get_table_from_file(file_name)
        title_list = ['id', 'name', 'email', 'subscribed']
        questions_asked = ['name: ', 'email: ', 'subscribed: ']
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
            get_longest_name_id(table)
        elif option == "6":
            get_subscribed_emails(table)
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

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code

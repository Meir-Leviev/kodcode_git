import data as d
import utils


def add_soldier(soldier_id: int, name: str) -> None:
    """
    Adds a new soldier to the system.

    Type: Business Logic

    Args:
        soldier_id (int): Soldier's personal number (ID)
        name (str): Soldier's name

    Returns:
        None - The function adds the soldier or raises an exception

    Raises:
        ValueError: If ID already exists in the system
        ValueError: If name is empty or invalid

    Reason for existence:
    Pure business logic for adding a soldier.
    Performs validation checks and adds the soldier to the data.
    Does not handle I/O - only logic.
    Raises exceptions in case of an error instead of returning False.
    """
    if not utils.is_valid_name(name):
        raise ValueError('Invalid name')

    if utils.find_soldier_by_id(soldier_id) is not None:
        raise ValueError('ID already exists')

    soldier_dict = {
        'id': soldier_id,
        'name': name,
        'duties': []
    }
    d.soldiers_list.append(soldier_dict)


def remove_soldier(soldier_id: int) -> None:
    """
    Removes a soldier from the system by ID.

    Type: Business Logic

    Args:
        soldier_id (int): Soldier's personal number (ID)

    Returns:
        None - The function removes the soldier or raises an exception

    Raises:
        KeyError: If a soldier with this ID is not found in the system

    Reason for existence:
    Business logic for removing a soldier.
    Checks for existence and removes from the data.
    Raises an exception if the soldier does not exist.
    """
    for soldier in d.soldiers_list:
        if soldier['id'] == soldier_id:
            d.soldiers_list.remove(soldier)
            return
    raise KeyError(f'id {soldier_id} not found')


def get_all_soldiers() -> list:
    """
    Returns the list of all soldiers in the system.

    Type: Data Access

    Args: None

    Returns:
        list: A list of dictionaries, each representing a soldier
              Empty list if there are no soldiers

    Raises: None - Always returns a list (empty or populated)

    Reason for existence:
    Controlled data access.
    Allows getting the data without directly accessing the global variable.
    """
    return d.soldiers_list

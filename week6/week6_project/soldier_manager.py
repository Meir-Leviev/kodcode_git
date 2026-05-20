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
    pass


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
    pass


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
    pass

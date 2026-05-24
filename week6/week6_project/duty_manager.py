import utils


def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    """
    Adds a new duty to a soldier.

    Type: Business Logic

    Args:
        soldier_id (int): Soldier's personal number (ID)
        duty_name (str): Name of the duty
        day (str): Day of the week (sunday/monday/tuesday/wednesday/thursday)

    Returns:
        None - The function adds the duty or raises an exception

    Raises:
        KeyError: If a soldier with this ID is not found in the system
        ValueError: If a duty with this name already exists for the soldier
        ValueError: If day is invalid (friday/saturday or an invalid value)

    Reason for existence:
    Business logic for adding a duty.
    Performs validations and adds a duty to the soldier.
    Raises exceptions in case of an error instead of returning False.
    """

    if not utils.is_valid_day(day):
        raise ValueError('Invalid day')

    soldier = utils.find_soldier_by_id(soldier_id)
    if soldier is None:
        raise ValueError('Soldier not found in the system')

    if utils.find_duty_by_name(soldier['duties'], duty_name) is not None:
        raise ValueError('Soldier has this duty')
    duty = {
        'name': duty_name,
        'day': day,
        'status': "pending"
    }
    soldier['duties'].append(duty)


def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    """
    Updates the status of a duty.

    Type: Business Logic

    Args:
        soldier_id (int): Soldier's personal number (ID)
        duty_name (str): Name of the duty
        new_status (str): New status (pending/completed/missed)

    Returns:
        None - The function updates the status or raises an exception

    Raises:
        KeyError: If a soldier with this ID is not found in the system
        KeyError: If a duty with this name is not found for the soldier
        ValueError: If new_status is invalid (not pending/completed/missed)

    Reason for existence:
    Business logic for updating status.
    Performs validations and updates the status.
    Raises exceptions in case of an error instead of returning False.
    """
    if not utils.is_valid_status(new_status):
        raise ValueError('New status is invalid')

    soldier = utils.find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError('Soldier not found')
    duty = utils.find_duty_by_name(soldier['duties'], duty_name)
    if duty is None:
        raise KeyError('Duty not found')
    duty['status'] = new_status


def get_soldier_duties(soldier_id: int) -> list:
    """
    Returns the list of a soldier's duties.

    Type: Data Access

    Args:
        soldier_id (int): Soldier's personal number (ID)

    Returns:
        list: List of duties (dictionaries)
              Empty list if there are no duties

    Raises:
        KeyError: If a soldier with this ID is not found in the system

    Reason for existence:
    Controlled access to a soldier's duties.
    Separates the data from the access to it.
    Raises an exception if the soldier does not exist
    (instead of returning an empty list).
    """
    soldier = utils.find_soldier_by_id(soldier_id)
    return soldier['duties']

import data as d


def find_soldier_by_id(soldier_id: int) -> dict | None:
    """
    Searches for a soldier by ID and returns it.

    Type: Helper Function

    Args:
        soldier_id (int): Soldier's personal number (ID)

    Returns:
        dict | None: The soldier's dictionary if found, None if not found

    Raises: None - returns None if not found

    Reason for existence:
    This function is used in many places in the system (DRY).
    Instead of repeating a search loop in every function,
    there is one function that handles it.
    Returns None instead of raising an exception - allows flexibility.
    """
    for soldier in d.soldiers_list:
        if soldier["id"] == soldier_id:
            return soldier
    return None


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    """
    Searches for a duty by name in a list of duties.

    Type: Helper Function

    Args:
        duties (list): List of duties
        duty_name (str): Name of the duty to search for

    Returns:
        dict | None: The duty dictionary if found, None if not found

    Raises: None - returns None if not found

    Reason for existence:
    This function is used in several places (adding a duty, updating status).
    Centralizes the search logic in one place.
    Returns None instead of raising an exception - allows flexibility.
    """
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
    return None


def is_valid_status(status: str) -> bool:
    """
    Checks if a status is valid.

    Type: Validation function

    Args:
        status (str): The status to check

    Returns:
        bool: True if the status is valid (pending/completed/missed)
              False if invalid

    Raises: None - always returns a bool

    Reason for existence:
    Status validation is used in several places.
    Instead of repeating the check, there is one function.
    It also makes it easier to change valid statuses in the future.
    Validation functions return a bool and do not raise exceptions.
    """
    valid = ['pending', 'completed', 'missed', ]
    return status in valid


def is_valid_name(name: str) -> bool:
    """
    Checks if a name is valid (not empty).

    Type: Validation function

    Args:
        name (str): The name to check

    Returns:
        bool: True if the name is valid (not empty)
              False if empty

    Raises: None - always returns a bool

    Reason for existence:
    Name validation is used in several places.
    Centralizes the validation logic in one place.
    In the future, additional checks can be added (minimum length,
    valid characters).
    Validation functions return a bool and do not raise exceptions.
    """
    cleaned_name = name.strip()
    if not cleaned_name:
        return False

    name_parts = cleaned_name.split()
    for part in name_parts:
        if not part.isalpha():
            return False
    return True


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    """
    Checks if a soldier has a duty with a specific name.

    Type: Validation function

    Args:
        soldier (dict): Soldier's dictionary
        duty_name (str): Name of the duty to check

    Returns:
        bool: True if the duty exists for the soldier
              False if it does not exist

    Raises: None - always returns a bool

    Reason for existence:
    This check is used when adding a duty (to prevent duplicates).
    Centralizes the logic in one place.
    Validation functions return a bool and do not raise exceptions.
    """
    for duty in soldier["duties"]:
        if duty_name == duty["name"]:
            return True
    return False


def is_valid_day(day: str) -> bool:
    """
    Checks if a day is valid (not Friday or Saturday).

    Type: Validation function

    Args:
        day (str): The day to check

    Returns:
        bool: True if the day is valid (sunday-thursday)
              False if invalid or forbidden (friday/saturday or invalid value)

    Raises: None - always returns a bool

    Reason for existence:
    Day validation is used when adding a duty.
    Centralizes the validation logic in one place.
    In the future, the valid days can be changed in one place.
    Validation functions return a bool and do not raise exceptions.
    """
    valid_days = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
    return day.lower() in valid_days

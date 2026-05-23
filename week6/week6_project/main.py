import soldier_manager as sm
import duty_manager as dm


def show_menu() -> None:
    """
    Displays the main menu to the user.

    Args: None
    Returns: None (Prints to the console)

    Reason for existence:
    Separates the menu display from the business logic.
    If we want to change the display later, we only change it here.
    """
    print("\n--- Soldier Management System ---")
    print("1. Add a new soldier")
    print("2. Remove a soldier")
    print("3. View all soldiers")
    print("4. Add a duty to a soldier")
    print("5. Update duty status")
    print("6. View a soldier's duties")
    print("7. Exit")
    print("---------------------------------")


def get_user_choice() -> str:
    """
    Gets the user's choice.

    Args: None
    Returns: A string representing the user's choice.

    Reason for existence:
    Separates getting user input from the logic of processing the choice.
    Allows swapping out the input method in the future (e.g., for a GUI).
    """
    choice = input("Please enter your input -> ")
    return choice


def handle_add_soldier() -> None:
    """
    Handles the process of adding a new soldier.
    Gets input from the user and calls the appropriate functions.

    Args: None
    Returns: None

    Reason for existence:
    Separates I/O from the business logic.
    main.py is responsible for user interaction,
    soldier_manager.py is responsible for the logic.
    """
    print("Soldier ID:")
    soldier_id = get_user_choice()
    print("Soldier name:")
    soldier_name = get_user_choice()
    try:
        sm.add_soldier(soldier_id, soldier_name)
        print('Soldier added successfully!')
    except ValueError as e:
        print(f'Error: {e}')


def handle_remove_soldier() -> None:
    """
    Handles the process of removing a soldier.
    Gets input from the user and calls the appropriate functions.

    Args: None
    Returns: None

    Reason for existence:
    Separates the UI from the business logic.
    """
    print('To remove a soldier enter soldier ID')
    soldier_id = get_user_choice()
    try:
        sm.remove_soldier(soldier_id)
        print('Soldier removed successfully!')
    except KeyError as e:
        print(f'Error: {e}')


def handle_view_soldiers() -> None:
    """
    Handles the process of displaying all soldiers.
    Calls the appropriate function and displays the result.

    Args: None
    Returns: None

    Reason for existence:
    Separates data retrieval from its presentation.
    """
    soldiers = sm.get_all_soldiers()
    print(soldiers)


def handle_add_duty() -> None:
    """
    Handles the process of adding a duty to a soldier.
    Gets input from the user and calls the appropriate functions.

    Args: None
    Returns: None

    Reason for existence:
    Separates the UI from the business logic.
    """
    print("Soldier ID:")
    soldier_id = get_user_choice()
    print("Duty name:")
    duty_name = get_user_choice()
    print('Day:')
    day = get_user_choice()
    try:
        dm.add_duty_to_soldier(soldier_id, duty_name, day)
        print('Duty added successfully!')
    except ValueError as e:
        print(f'Error: {e}')


def handle_update_duty_status() -> None:
    """
    Handles the process of updating a duty's status.
    Gets input from the user and calls the appropriate functions.

    Args: None
    Returns: None

    Reason for existence:
    Separates the UI from the business logic.
    """
    print("Soldier ID:")
    soldier_id = get_user_choice()
    print("Duty name:")
    duty_name = get_user_choice()
    print('New status:')
    status = get_user_choice()
    try:
        dm.update_duty_status(soldier_id, duty_name, status)
        print('Update successfully!')
    except ValueError as e:
        print(f'Error: {e}')
    except KeyError as e:
        print(f'Error: {e}')


def handle_view_soldier_duties() -> None:
    """
    Handles the process of displaying a soldier's duties.
    Gets input from the user and calls the appropriate functions.

    Args: None
    Returns: None

    Reason for existence:
    Separates the UI from the business logic.
    """
    print("Soldier ID:")
    soldier_id = get_user_choice()
    duties = dm.get_soldier_duties(soldier_id)
    print(duties)


def main() -> None:
    """
    The main function of the program.
    Runs the main loop that displays a menu, gets a choice, and executes an action.

    Args: None
    Returns: None

    Reason for existence:
    The entry point of the program. Manages the primary execution flow.
    """
    pass

import os


def save_backup(tasks):
    save_tasks('backup_tasks.txt', tasks)


def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    tasks = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split('|')
            task = {
                'id': line[0],
                'status': line[1],
                'desc': line[2]
            }
            tasks.append(task)
    return tasks


def save_tasks(filename: str, tasks: list[dict]):
    save_backup(tasks)
    with open(filename, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(f"{task['id']}|{task['status']}|{task['desc']}\n")


def add_task(filename, description):
    tasks = load_tasks(filename)
    new_id = 1
    if len(tasks) > 0:
        last_id = int(tasks[-1]['id'])
        new_id = last_id + new_id

    new_task = {
        'id': new_id,
        'status': 'PENDING',
        'desc': description
    }
    tasks.append(new_task)
    save_tasks(filename, tasks)


def complete_task(filename, task_id):
    tasks = load_tasks(filename)
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'DONE'
    save_tasks(filename, tasks)


def list_tasks(filename):
    tasks = load_tasks(filename)
    for task in tasks:
        status = '[ ]'
        if task['status'] == 'DONE':
            status = '[✓]'

        print(f"{status} {task['id']} | {task['desc']}")


def remove_task(filename, task_id: str):
    tasks = load_tasks(filename)
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(filename, tasks)
            return
    print('Task not found')
    return


def show_filter_by_status(filename):
    tasks = load_tasks(filename)
    sorted_tasks = sorted(tasks, key=lambda task:
                          0 if task['status'] == 'DONE' else 1)
    print('--- Sorted Tasks ---')
    for task in sorted_tasks:
        status_icon = '[✓]' if task['status'] == 'DONE' else '[ ]'
        print(f"{status_icon} {task['id']} | {task['desc']}")


def search_by_id(filename, task_id):
    tasks = load_tasks(filename)
    for task in tasks:
        if task['id'] == task_id:
            print(task)


def show_stats(filename):
    tasks = load_tasks(filename)
    cnt_complete = 0
    cnt_pending = 0
    for task in tasks:
        if tasks['status'] == 'DONE':
            cnt_complete += 1
        else:
            cnt_pending += 1
    print('--- Stats ---')
    print(f'completed tasks: {cnt_complete}')
    print(f'pending tasks: {cnt_pending}')


def main():
    FILENAME = "tasks.txt"
    while True:
        print('\n=== To-Do List Manager ===')
        print('1. View Tasks')
        print('2. Add Task')
        print('3. Mark as Completed')
        print('4. Remove task')
        print('5. View sorted tasks')
        print('6. Search by id')
        print('7. Show Stats')
        print('"q". Exit')
        choice = input('Choice: ')

        if choice == '1':
            list_tasks(FILENAME)
        elif choice == '2':
            desc = input('Task description: ')
            add_task(FILENAME, desc)
            print('Task added!')
        elif choice == '3':
            task_id = input('Task number: ')
            complete_task(FILENAME, task_id)
        elif choice == '4':
            task_id = input('Task number: ')
            remove_task(FILENAME, task_id)
        elif choice == '5':
            show_filter_by_status(FILENAME)
        elif choice == '6':
            task_id = input('Task number: ')
            search_by_id(FILENAME, task_id)
        elif choice == '7':
            show_stats(FILENAME)
        elif choice == 'q':
            print('Goodbye!')
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()

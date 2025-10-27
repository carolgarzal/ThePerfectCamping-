import pandas as pd

# we assume the same global DataFrame from your add_task file
to_do_list = pd.DataFrame(columns=['to_bring', 'priority', 'use', 'deadline'])

def remove_task():
    global to_do_list  

    if to_do_list.empty:
        print(" Your camping list is empty, nothing to remove.\n")
        return

    print("\n📋 Current tasks:")
    print(to_do_list[['to_bring', 'priority', 'use', 'deadline']])

    # Ask which task to remove
    task_name = input("\nEnter the name of the task to remove: ")

    # Look for the task (case-insensitive)
    mask = to_do_list['to_bring'].str.lower() == task_name.lower()

    if mask.any():
        to_do_list = to_do_list[~mask]
        print(f"\n Task '{task_name}' was removed successfully.\n")
    else:
        print(f"\n Task '{task_name}' not found in your list.\n")

    print("📋 Updated list:")
    print(to_do_list)
 
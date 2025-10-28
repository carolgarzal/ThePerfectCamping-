import pandas as pd
from datetime import datetime

to_do_list = pd.DataFrame(columns=['to_bring', 'priority', 'use', 'deadline'])

def add_task(df=None):
    global to_do_list
    if df is not None:
        to_do_list = df

    to_bring = input("What do you need to do or buy for camping: ")
    priority = input("Priority (high / medium / low): ").lower()
    use = input("What is it used for (camping / eating / clothing / excursion): ").lower()
    deadline_input = input("Deadline (YYYY-MM-DD): ")

    try:
        deadline = datetime.strptime(deadline_input, "%Y-%m-%d").date()
    except ValueError:
        print("⚠️ Invalid date format. Use YYYY-MM-DD.")
        return to_do_list

    new_task = pd.DataFrame({
        'to_bring': [to_bring],
        'priority': [priority],
        'use': [use],
        'deadline': [deadline]
    })

    to_do_list = pd.concat([to_do_list, new_task], ignore_index=True)
    print(f"\n✅ '{to_bring}' added correctly!\n")

    return to_do_list

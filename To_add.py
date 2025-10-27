import pandas as pd
from datetime import date, datetime

#Create empty Dataframe 
to_do_list = pd.DataFrame(columns=['to_bring', 'priority', 'use', 'deadline'])

def add_task():
    global to_do_list  

    # We ask for the information to the user 
    to_bring = input("What do you need to do or buy for camping")
    priority = input("Priority (high / medium / low): ").lower()
    use = input("What is it used for (camping / eating / clothing / excursion): ").lower()
    deadline_input = input("Deadline to have it ready (YYYY-MM-DD): ")

    # Convert date 
    try:
        deadline = datetime.strptime(deadline_input, "%Y-%m-%d").date()
    except ValueError:
        print("⚠️ Incorrect format.")
       
    # Create a new row
    new_task = pd.DataFrame({
        'to_bring': [to_bring],
        'priority': [priority],
        'use': [use],
        'deadline': [deadline]
    })

    # Add to main dataframe
    to_do_list = pd.concat([to_do_list, new_task], ignore_index=True)

    print(f"\n✅ '{to_bring}' added correctly.\n")

add_task()

print("To do list:")
print(to_do_list)

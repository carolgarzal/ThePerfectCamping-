import sys
import pandas as pd

import To_add as data_mod
from view_tasks import view_tasks
from suggest_tasks import suggest_tasks
from removetaskcaro import remove_task

def menu():
    while True:
        print("\n🏕️ PERFECT CAMPING PLANNER")
        print("1) Add task")
        print("2) View tasks")
        print("3) Remove task")
        print("4) Suggest tasks")
        print("5) Exit")
        option = input("Choose (1-5): ").strip()

        if option == "1":
            data_mod.add_task()

        elif option == "2":
            view_tasks(data_mod.to_do_list)

        elif option == "3":
            updated = remove_task(data_mod.to_do_list)
            if isinstance(updated, pd.DataFrame):
                data_mod.to_do_list = updated

        elif option == "4":
            suggest_tasks(data_mod.to_do_list)

        elif option == "5":
            print("Bye! 🌄")
            sys.exit(0)
        else:
            print("⚠️ Invalid option. Choose 1–5.\n")

if __name__ == "__main__":
    menu()

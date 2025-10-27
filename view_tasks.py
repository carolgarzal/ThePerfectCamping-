import pandas as pd

PRIORITY_ORDER = pd.CategoricalDtype(categories=['high', 'medium', 'low'], ordered=True)

def view_tasks(df: pd.DataFrame) -> None:
    """
    Muestra las tareas ordenadas por prioridad (high→medium→low)
    y luego por fecha (la más próxima primero). Si no hay tareas, lo dice.
    """
    if df.empty:
        print("📭 Your camping list is empty.\n")
        return

    tmp = df.copy()
    tmp['priority'] = tmp['priority'].astype(PRIORITY_ORDER)
    tmp['deadline'] = pd.to_datetime(tmp['deadline'], errors='coerce')

    tmp = tmp.sort_values(
        by=['priority', 'deadline'],
        ascending=[True, True],
        na_position='last'  # sin fecha al final
    )

    print("\n📝 Camping To-Do List (sorted by priority, then deadline):")
    for _, row in tmp.iterrows():
        dl = row['deadline']
        dl_str = dl.date().isoformat() if pd.notna(dl) else "—"
        print(f"• {row['to_bring']} | {row['priority']} | {row['use']} | {dl_str}")
    print()

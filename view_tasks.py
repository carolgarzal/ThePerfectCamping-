def view_tasks(df):
    if df is None or df.empty:
        print("⚠️ Your list is empty.\n")
        return

    prio_order = {'high': 0, 'medium': 1, 'low': 2}
    df_sorted = df.copy()
    df_sorted['__prio'] = df_sorted['priority'].map(prio_order).fillna(9)
    df_sorted = df_sorted.sort_values(by=['__prio', 'deadline']).drop(columns='__prio')

    print("\n📋 Camping Tasks:")
    print(df_sorted[['to_bring', 'priority', 'use', 'deadline']].to_string(index=False))
    print()

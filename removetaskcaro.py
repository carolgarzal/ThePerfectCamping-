def remove_task(df):
    if df is None or df.empty:
        print("⚠️ Your list is empty. Nothing to remove.\n")
        return df

    print("\nCurrent tasks:")
    print(df[['to_bring', 'priority', 'use', 'deadline']].to_string(index=False))

    name = input("\nEnter the name of the task to remove: ")
    mask = df['to_bring'].str.lower() == name.lower()

    if mask.any():
        updated = df[~mask].reset_index(drop=True)
        print(f"\n✅ Task '{name}' removed successfully!\n")
        return updated
    else:
        print(f"\n⚠️ Task '{name}' not found.\n")
        return df

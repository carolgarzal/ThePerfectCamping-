from datetime import date

def suggest_tasks(df):
    if df is None or df.empty:
        print("⚠️ No tasks to suggest.\n")
        return

    today = date.today()
    prio_points = {'high': 3, 'medium': 2, 'low': 1}

    temp = df.copy()
    temp['prio_pts'] = temp['priority'].map(prio_points).fillna(0)
    temp['days_left'] = (temp['deadline'] - today).dt.days
    temp['urgency_pts'] = temp['days_left'].apply(
        lambda d: 3 if d <= 2 else (2 if d <= 5 else 1)
    )

    temp['score'] = (temp['prio_pts'] * 0.7) + (temp['urgency_pts'] * 0.3)
    top = temp.sort_values('score', ascending=False).head(3)

    print("\n🤖 Suggested Tasks:")
    for _, r in top.iterrows():
        print(f"- {r['to_bring']} | {r['priority']} | {r['use']} | {r['deadline']} | score: {round(r['score'],2)}")
    print()

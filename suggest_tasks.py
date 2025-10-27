import pandas as pd
from datetime import date

def suggest_tasks(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    # Convertir prioridad en puntos numéricos
    priority_map = {'high': 3, 'medium': 2, 'low': 1}
    df['prio_points'] = df['priority'].map(priority_map)

    # Calcular urgencia según deadline
    today = pd.Timestamp.today().date()
    df['urgency_points'] = df['deadline'].apply(
        lambda d: 3 if pd.notna(d) and (d - today).days <= 2 else
                  2 if pd.notna(d) and (d - today).days <= 5 else
                  1 if pd.notna(d) else 0
    )

    # Calcular puntuación combinada
    df['score'] = (df['prio_points'] * 0.7) + (df['urgency_points'] * 0.3)

    # Ordenar y mostrar top N
    sorted_df = df.sort_values(by='score', ascending=False).head(top_n)
    print("🤖 Suggested Tasks (by priority & deadline):")
    for _, row in sorted_df.iterrows():
        print(f"• {row['to_bring']} | {row['priority']} | {row['use']} | {row['deadline']} | score={row['score']:.2f}")

    return sorted_df

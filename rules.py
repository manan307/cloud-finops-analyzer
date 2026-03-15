def detect_idle(df):
    idle = df[df["cpu_usage"] < 5]
    suggestions = []
    for i in idle.index:
        saving = df.loc[i,"cost"] * 0.8
        suggestions.append(
        {
            "resource": df.loc[i,"resource_id"],
            "issue": "Idle resource",
            "suggestion": "Stop or downsize instance",
            "estimated_saving": round(saving,2)
        }
        )
    return suggestions

def detect_cost_spike(df):
    daily = df.groupby("day")["cost"].sum()
    spikes = []
    for i in range(1,len(daily)):
        prev = daily.iloc[i-1]
        today = daily.iloc[i]
        if today > prev * 1.3:
            spikes.append({
                "day": i+1,
                "issue": "Cost Spike Detected",
                "previous_cost": prev,
                "today_cost": today
            })

    return spikes
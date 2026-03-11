import pandas as pd

# Sample football dataset
data = {
    "Team": ["Arsenal", "Chelsea", "Liverpool", "Man City", "Arsenal", "Liverpool"],
    "Goals": [2, 1, 3, 4, 1, 2],
    "Opponent": ["Chelsea", "Arsenal", "Man City", "Liverpool", "Man City", "Chelsea"]
}

df = pd.DataFrame(data)

# Total goals by team
goals_by_team = df.groupby("Team")["Goals"].sum()

print("Total Goals by Team:")
print(goals_by_team)

# Average goals per match
average_goals = df["Goals"].mean()

print("\nAverage Goals per Match:")
print(average_goals)

# Best scoring team
best_team = goals_by_team.idxmax()

print("\nBest Attacking Team:")
print(best_team)

# Find highest scoring match
highest_match = df.loc[df["Goals"].idxmax()]

print("\nHighest Scoring Performance:")
print(highest_match)
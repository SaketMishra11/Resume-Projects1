import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the 'visuals' directory exists
if not os.path.exists('visuals'):
    os.makedirs('visuals')

# Load datasets
matches = pd.read_csv("matches.csv")

# Clean 'matches.csv'
matches['date'] = pd.to_datetime(matches['date'])
matches = matches.dropna(subset=['winner'])

# Standardize team names
team_name_map = {
    'Rising Pune Supergiants': 'Rising Pune Supergiant',
    'Delhi Daredevils': 'Delhi Capitals',
    'Deccan Chargers': 'Sunrisers Hyderabad'
}
matches.replace({'team1': team_name_map, 'team2': team_name_map,
                 'toss_winner': team_name_map, 'winner': team_name_map}, inplace=True)

# 1. Matches won by each team
team_wins = matches['winner'].value_counts()

# Print the top 3 teams with ranks
top_3_teams = team_wins.head(3)
print(f"1st Position: {top_3_teams.index[0]} with {top_3_teams.values[0]} wins")
print(f"2nd Position: {top_3_teams.index[1]} with {top_3_teams.values[1]} wins")
print(f"3rd Position: {top_3_teams.index[2]} with {top_3_teams.values[2]} wins")

# 2. Calculate win percentage for each team
total_matches = len(matches)
team_win_percentage = (team_wins / total_matches) * 100

# 3. Season-wise analysis (optional improvement)
matches['season'] = matches['id'].apply(lambda x: x // 100)  # Assuming ID number format allows us to extract season
season_wins = matches.groupby(['season', 'winner']).size().unstack(fill_value=0)

# Plot the bar chart for matches won by each team
plt.figure(figsize=(12, 6))
sns.barplot(x=team_wins.index, y=team_wins.values, palette="mako")
plt.xticks(rotation=45)
plt.title("Matches Won by Each Team")
plt.ylabel("Wins")
plt.xlabel("Teams")
plt.tight_layout()

# Save the plot
plt.savefig("visuals/team_wins.png")
plt.show()

# Plot for win percentage
plt.figure(figsize=(12, 6))
sns.barplot(x=team_win_percentage.index, y=team_win_percentage.values, palette="viridis")
plt.xticks(rotation=45)
plt.title("Win Percentage of Each Team")
plt.ylabel("Win Percentage")
plt.xlabel("Teams")
plt.tight_layout()

# Save the plot
plt.savefig("visuals/team_win_percentage.png")
plt.show()

# Season-wise performance
season_wins.plot(kind='bar', stacked=True, figsize=(14, 8))
plt.title("Season-wise Team Performance")
plt.ylabel("Matches Won")
plt.xlabel("Season")
plt.tight_layout()

# Save the season-wise plot
plt.savefig("visuals/season_wise_performance.png")
plt.show()
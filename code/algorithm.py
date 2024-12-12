from itertools import combinations
import pandas as pd
from pandas.core.common import flatten


# Load and filter player data
df = pd.read_csv('fpl-form-predicted-points.csv')
pts_with_prob = df.columns[7]
appearing_prob = df.columns[6]
df['comparison_value'] = 2 * df[pts_with_prob] / 5 + 5 / df['Price']
filtered_df = df.loc[(df[appearing_prob] > 0.5) & (df[pts_with_prob] > 2)]


# Sort players by position and comparison value
fwd_players = filtered_df.loc[filtered_df['Pos'] == 'FWD'].sort_values(by='comparison_value', ascending=False)
mid_players = filtered_df.loc[filtered_df['Pos'] == 'MID'].sort_values(by='comparison_value', ascending=False).head(20)
def_players = filtered_df.loc[filtered_df['Pos'] == 'DEF'].sort_values(by='comparison_value', ascending=False).head(20)
gk_players = filtered_df.loc[filtered_df['Pos'] == 'GK'].sort_values(by='comparison_value', ascending=False)


# Function to calculate the sum of a column for a given set of players from the data
def players_sumof(players, data, column):
    return sum(data.loc[data['Name'].isin(players), column])


# Function to combine and sort players by a given column
def combine_sort_by(players, n, column):
    sorted_combinations = sorted(
        combinations(players['Name'], n),
        key=lambda combination: players_sumof(combination, players, column),
        reverse=True
    )
    return sorted_combinations


fwd_combinations = combine_sort_by(fwd_players, 3, 'comparison_value')
mid_combinations = combine_sort_by(mid_players, 5, 'comparison_value')
def_combinations = combine_sort_by(def_players, 5, 'comparison_value')
gk_combinations = combine_sort_by(gk_players, 2, 'comparison_value')


# Initial best team
best_team = list(flatten([fwd_combinations[0], mid_combinations[0], def_combinations[0], gk_combinations[0]]))


# Algorithm to choose the next best team
def choose_new_team(i, prev_team):
    new_teams = [
        list(flatten([fwd_combinations[i % len(fwd_combinations)], prev_team[3:8], prev_team[8:13], prev_team[13:]])),
        list(flatten([prev_team[:3], mid_combinations[i], prev_team[8:13], prev_team[13:]])),
        list(flatten([prev_team[:3], prev_team[3:8], def_combinations[i], prev_team[13:]])),
        list(flatten([prev_team[:3], prev_team[3:8], prev_team[8:13], gk_combinations[i % len(gk_combinations)]]))
    ]
    return max(new_teams, key=lambda team: players_sumof(team, filtered_df, pts_with_prob))


# Loop to find the best team
index = 1
current_price = players_sumof(best_team, filtered_df, 'Price')
current_points = players_sumof(best_team, filtered_df, pts_with_prob)
while index < 3000:
    next_team = choose_new_team(index, best_team)
    next_price = players_sumof(next_team, filtered_df, 'Price')
    if current_price <= 100:
        if next_price <= 100:
            current_points = players_sumof(best_team, filtered_df, pts_with_prob)
            next_points = players_sumof(next_team, filtered_df, pts_with_prob)
            if next_points > current_points:
                best_team = next_team
                current_price = next_price
        index += 1
    else:
        best_team = next_team
        current_price = next_price
        index += 1


# Find the best team possible, no price limit
best_fwd_combination = combine_sort_by(fwd_players, 3, pts_with_prob)[0]
best_mid_combination = combine_sort_by(mid_players, 5, pts_with_prob)[0]
best_def_combination = combine_sort_by(def_players, 5, pts_with_prob)[0]
best_gk_combination = combine_sort_by(gk_players, 2, pts_with_prob)[0]


highest_pts_team = list(flatten([best_fwd_combination, best_mid_combination, best_def_combination, best_gk_combination]))
highest_pts_team_points = players_sumof(highest_pts_team, filtered_df, pts_with_prob)
highest_pts_team_price = players_sumof(highest_pts_team, filtered_df, 'Price')


print(f'Best valid team found:\n{best_team}\nPrice: {current_price}\nPoints: {current_points}\nTeam with highest points possible:\n{highest_pts_team}\nPrice: {highest_pts_team_price}\nPoints: {highest_pts_team_points}\nTeam point difference: {highest_pts_team_points - current_points}')
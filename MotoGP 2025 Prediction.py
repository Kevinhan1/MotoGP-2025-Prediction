# -*- coding: utf-8 -*-
"""UAS Data Mining.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z4Uq5hL48a55zSYAwZOap4jLv0hHNwgW

***Line Up 2024***
"""

import pandas as pd

df = pd.read_excel('/content/drive/MyDrive/UAS Datamin/dataset motogp 2024.xlsx')
df

"""***Line Up 2025***"""

# prompt: tampilkan sheet Line Up 2025

import pandas as pd

# Assuming 'Line Up 2025' is a sheet name in your Excel file
df_lineup = pd.read_excel('/content/drive/MyDrive/UAS Datamin/dataset motogp 2024.xlsx', sheet_name='Line Up 2025')
df_lineup

# prompt: sprint saya ingin bagian Constructor diisi sesuai nama tim 2024

import pandas as pd

df = pd.read_excel('/content/drive/MyDrive/UAS Datamin/dataset motogp 2024.xlsx')
df

# Assuming 'Line Up 2025' is a sheet name in your Excel file
df_lineup = pd.read_excel('/content/drive/MyDrive/UAS Datamin/dataset motogp 2024.xlsx', sheet_name='Line Up 2024')

# Replace 'Constructor' column with team names from 'Line Up 2025'
# First, create a dictionary to map rider names to their teams
team_mapping = dict(zip(df_lineup['Rider'], df_lineup['Team']))

# Use the map function to replace Constructor values based on the mapping
df['Constructor'] = df['Rider'].map(team_mapping)

df

import pandas as pd
from IPython.display import display

# Path file Excel
file_path = '/content/drive/MyDrive/UAS Datamin/dataset motogp 2024.xlsx'

# Membaca sheet Race dan Line Up 2024
df_race = pd.read_excel(file_path, sheet_name='Sprint')
df_lineup = pd.read_excel(file_path, sheet_name='Line Up 2024')

# Membuat mapping Rider ke Team dari sheet Line Up 2024
team_mapping = dict(zip(df_lineup['Rider'], df_lineup['Team']))

# Memperbarui kolom Constructor pada sheet Race
df_race['Constructor'] = df_race['Rider'].map(team_mapping)

# Filter untuk race QAT
qat_race = df_race[df_race['event'] == 'QAT'].copy()

# Konversi posisi ke numerik, jika tidak numerik maka menjadi NaN
qat_race['numeric_pos'] = pd.to_numeric(qat_race['pos.'], errors='coerce')

# Pisahkan data yang posisi numeriknya valid dan yang "DNF"
numerics = qat_race[qat_race['numeric_pos'].notna()].sort_values('numeric_pos')
non_numerics = qat_race[qat_race['numeric_pos'].isna()]

# Gabungkan kembali data numerik dan non-numerik dengan DNF di bawah
qat_race_sorted = pd.concat([numerics, non_numerics], ignore_index=True).drop(columns=['numeric_pos'])

# Menampilkan hasil dalam bentuk tabel rapi
display(qat_race_sorted)

import pandas as pd
from IPython.display import display

# Path file Excel
file_path = '/content/drive/MyDrive/UAS Datamin/dataset motogp 2024.xlsx'

# Membaca sheet Race dan Line Up 2024
df_race = pd.read_excel(file_path, sheet_name='Race')
df_lineup = pd.read_excel(file_path, sheet_name='Line Up 2024')

# Membuat mapping Rider ke Team dari sheet Line Up 2024
team_mapping = dict(zip(df_lineup['Rider'], df_lineup['Team']))

# Memperbarui kolom Constructor pada sheet Race
df_race['Constructor'] = df_race['Rider'].map(team_mapping)

# Filter untuk race QAT
qat_race = df_race[df_race['event'] == 'QAT'].copy()

# Konversi posisi ke numerik, jika tidak numerik maka menjadi NaN
qat_race['numeric_pos'] = pd.to_numeric(qat_race['pos.'], errors='coerce')

# Pisahkan data yang posisi numeriknya valid dan yang "DNF"
numerics = qat_race[qat_race['numeric_pos'].notna()].sort_values('numeric_pos')
non_numerics = qat_race[qat_race['numeric_pos'].isna()]

# Gabungkan kembali data numerik dan non-numerik dengan DNF di bawah
qat_race_sorted = pd.concat([numerics, non_numerics], ignore_index=True).drop(columns=['numeric_pos'])

# Menampilkan hasil dalam bentuk tabel rapi
display(qat_race_sorted)

import pandas as pd

# Load data from Excel
file_path = '/content/drive/MyDrive/UAS Datamin/dataset motogp 2024.xlsx'

# Read the 'Sprint' and 'Race' sheets
df_sprint = pd.read_excel(file_path, sheet_name='Sprint')
df_race = pd.read_excel(file_path, sheet_name='Race')
df_lineup = pd.read_excel(file_path, sheet_name='Line Up 2024')

# Create a mapping of teams to constructors from the Line Up 2024 data
team_mapping = dict(zip(df_lineup['Rider'], df_lineup['Constructor']))

# Fill empty Constructor columns in both sheets
df_sprint['Constructor'] = df_sprint['Constructor'].fillna(df_sprint['Rider'].map(team_mapping))
df_race['Constructor'] = df_race['Constructor'].fillna(df_race['Rider'].map(team_mapping))

# Display the updated tables
print("Tabel Sprint Setelah Diperbarui:")
display(df_sprint)
print("Tabel Race Setelah Diperbarui:")
display(df_race)

"""# ***EDA***

# ***Sprint***
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data from the 'Race' sheet
file_path = '/content/drive/MyDrive/UAS Datamin/dataset_motogp_updated.xlsx'
race_data = pd.read_excel(file_path, sheet_name='Sprint')

# Filter Out Invalid Points (Maximum 12 for Race)
race_data = race_data[race_data['pts'] <= 12]

# Team Colors
default_color = "#808080"
team_colors = {
    "Ducati Lenovo Team": "#cc0101",
    "Prima Pramac Racing": "#8532c5",
    "Aprilia Racing": "#5bb33a",
    "Gresini Racing MotoGP": "#9fb2da",
    "CASTROL Honda LCR": "#dddddd",
    "IDEMITSU Honda LCR": "#dddddd",
    "Monster Energy Yamaha MotoGP Team": "#0b2d81",
    "Pertamina Enduro VR46 Racing Team": "#e1fa52",
    "Red Bull KTM Factory Racing": "#d55e2b",
    "Repsol Honda Team": "#fea111",
    "Red Bull GASGAS Tech3": "#990625",
    "Trackhouse Racing": "#0256ba",
    "Pertamina Enduro VR46 MotoGP Team": "#e1fa52",
    "Yamaha Factory Racing Team": "#0b2d81",
    "HRC Test Team": "#dddddd"
}

# Ensure all teams have colors
race_data.loc[:, 'Team_Color'] = race_data['Team'].map(team_colors).fillna(default_color)

# Display Basic Information as Table
basic_info = pd.DataFrame({
    "Attribute": ["Shape", "Columns"],
    "Value": [str(race_data.shape), ", ".join(race_data.columns.tolist())]
})
print("Basic Information:")
print(basic_info.to_markdown(index=False))

# Data Cleaning Suggestions
race_data.loc[:, 'time / gap'] = race_data['time / gap'].fillna('N/A')
race_data.loc[:, 'Constructor'] = race_data['Constructor'].fillna('Unknown')

# Count of Unique Riders per Team
rider_counts = race_data.groupby('Team')['Rider'].nunique().reset_index()
rider_counts.columns = ['Team', 'Unique Rider Count']
print("\nCount of Unique Riders per Team:")
print(rider_counts.to_markdown(index=False))

# Plotting the Count of Unique Riders per Team
plt.figure(figsize=(12, 8))
sns.barplot(x='Unique Rider Count', y='Team', data=rider_counts, hue='Team', palette=team_colors, dodge=False, legend=False)
plt.title('Count of Unique Riders per Team', fontsize=16)
plt.xlabel('Number of Unique Riders', fontsize=12)
plt.ylabel('Team', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

# Average Points by Team
avg_points_team = race_data.groupby('Team')['pts'].mean().reset_index()
print("\nAverage Points by Team:")
print(avg_points_team.to_markdown(index=False))

# Plotting Average Points by Team
plt.figure(figsize=(12, 8))
sns.barplot(x='pts', y='Team', data=avg_points_team, hue='Team', palette=team_colors, dodge=False, legend=False)
plt.title('Average Points by Team', fontsize=16)
plt.xlabel('Average Points', fontsize=12)
plt.ylabel('Team', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

# Top 5 Riders by Total Points in Race
total_points_riders = race_data.groupby('Rider')['pts'].sum().reset_index()
top_5_points_riders = total_points_riders.sort_values(by='pts', ascending=False).head(5)

# Merge to get the team colors for the top 5 riders
top_5_points_riders = top_5_points_riders.merge(race_data[['Rider', 'Team_Color']], on='Rider', how='left').drop_duplicates()

# Drop the Team_Color column before printing the table
top_5_points_riders_display = top_5_points_riders.drop(columns=['Team_Color'])

# Print the table without Team_Color
print("\nTop 5 Riders by Total Points in Race:")
print(top_5_points_riders_display.to_markdown(index=False))

# Create a dictionary mapping each Rider to their corresponding Team_Color (for plotting)
rider_color_map = dict(zip(top_5_points_riders['Rider'], top_5_points_riders['Team_Color']))

# Plotting Top 5 Riders by Total Points in Race
plt.figure(figsize=(12, 8))
sns.barplot(
    x='pts',
    y='Rider',
    data=top_5_points_riders,
    palette=rider_color_map,  # Use the color map here
    dodge=False,
    legend=False
)
plt.title('Top 5 Riders by Total Points in Race', fontsize=16)
plt.xlabel('Total Points', fontsize=12)
plt.ylabel('Rider', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()


# Ensure 'pos.' column is numeric
race_data['pos.'] = pd.to_numeric(race_data['pos.'], errors='coerce')

# Check for any NaN values after conversion (which means invalid positions)
print(race_data['pos.'].isna().sum())

# Now filter riders who finished in positions 1, 2, 3, 4, or 5
top_positions_riders = race_data[race_data['pos.'].isin([1, 2, 3, 4, 5])]

# Check if the filtered data has any rows
if top_positions_riders.empty:
    print("No riders finished in positions 1 to 5.")
else:
    # Count the occurrences of each rider in the top positions
    top_positions_counts = top_positions_riders.groupby('Rider')['pos.'].count().reset_index()
    top_positions_counts.columns = ['Rider', 'Count in Top 5']

    # Merge with team colors
    top_positions_counts = top_positions_counts.merge(race_data[['Rider', 'Team_Color']].drop_duplicates(), on='Rider', how='left')

    # Drop the Team_Color column before printing
    top_positions_counts_display = top_positions_counts.drop(columns=['Team_Color'])

    # Sort by the count in descending order and select the top 5 riders
    top_5_riders_by_top_positions = top_positions_counts_display.sort_values(by='Count in Top 5', ascending=False).head(5)

    # Print the table without Team_Color
    print("\nTop 5 Riders by Frequency of Finishing in Positions 1 to 5:")
    print(top_5_riders_by_top_positions.to_markdown(index=False))

    # Create a dictionary mapping each Rider to their corresponding Team_Color (for plotting)
    top_positions_color_map = dict(zip(top_positions_counts['Rider'], top_positions_counts['Team_Color']))

    # Plotting Top 5 Riders by Frequency of Finishing in Positions 1 to 5
    plt.figure(figsize=(12, 8))
    sns.barplot(
        x='Count in Top 5',
        y='Rider',
        data=top_5_riders_by_top_positions,
        palette=top_positions_color_map,  # Use the color map here
        dodge=False,
        legend=False
    )
    plt.title('Top 5 Riders by Frequency of Finishing in Positions 1 to 5', fontsize=16)
    plt.xlabel('Count of Top 5 Finishes', fontsize=12)
    plt.ylabel('Rider', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
plt.show()

"""# ***Race***"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data from the 'Race' sheet
file_path = '/content/drive/MyDrive/UAS Datamin/dataset_motogp_updated.xlsx'
race_data = pd.read_excel(file_path, sheet_name='Race')

# Filter Out Invalid Points (Maximum 12 for Race)
race_data = race_data[race_data['pts'] <= 12]

# Team Colors
default_color = "#808080"
team_colors = {
    "Ducati Lenovo Team": "#cc0101",
    "Prima Pramac Racing": "#8532c5",
    "Aprilia Racing": "#5bb33a",
    "Gresini Racing MotoGP": "#9fb2da",
    "CASTROL Honda LCR": "#dddddd",
    "IDEMITSU Honda LCR": "#dddddd",
    "Monster Energy Yamaha MotoGP Team": "#0b2d81",
    "Pertamina Enduro VR46 Racing Team": "#e1fa52",
    "Red Bull KTM Factory Racing": "#d55e2b",
    "Repsol Honda Team": "#fea111",
    "Red Bull GASGAS Tech3": "#990625",
    "Trackhouse Racing": "#0256ba",
    "Pertamina Enduro VR46 MotoGP Team": "#e1fa52",
    "Yamaha Factory Racing Team": "#0b2d81",
    "HRC Test Team": "#dddddd"
}

# Ensure all teams have colors
race_data.loc[:, 'Team_Color'] = race_data['Team'].map(team_colors).fillna(default_color)

# Display Basic Information as Table
basic_info = pd.DataFrame({
    "Attribute": ["Shape", "Columns"],
    "Value": [str(race_data.shape), ", ".join(race_data.columns.tolist())]
})
print("Basic Information:")
print(basic_info.to_markdown(index=False))

# Data Cleaning Suggestions
race_data.loc[:, 'time / gap'] = race_data['time / gap'].fillna('N/A')
race_data.loc[:, 'Constructor'] = race_data['Constructor'].fillna('Unknown')

# Count of Unique Riders per Team
rider_counts = race_data.groupby('Team')['Rider'].nunique().reset_index()
rider_counts.columns = ['Team', 'Unique Rider Count']
print("\nCount of Unique Riders per Team:")
print(rider_counts.to_markdown(index=False))

# Plotting the Count of Unique Riders per Team
plt.figure(figsize=(12, 8))
sns.barplot(x='Unique Rider Count', y='Team', data=rider_counts, hue='Team', palette=team_colors, dodge=False, legend=False)
plt.title('Count of Unique Riders per Team', fontsize=16)
plt.xlabel('Number of Unique Riders', fontsize=12)
plt.ylabel('Team', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

# Average Points by Team
avg_points_team = race_data.groupby('Team')['pts'].mean().reset_index()
print("\nAverage Points by Team:")
print(avg_points_team.to_markdown(index=False))

# Plotting Average Points by Team
plt.figure(figsize=(12, 8))
sns.barplot(x='pts', y='Team', data=avg_points_team, hue='Team', palette=team_colors, dodge=False, legend=False)
plt.title('Average Points by Team', fontsize=16)
plt.xlabel('Average Points', fontsize=12)
plt.ylabel('Team', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

# Top 5 Riders by Total Points in Race
total_points_riders = race_data.groupby('Rider')['pts'].sum().reset_index()
top_5_points_riders = total_points_riders.sort_values(by='pts', ascending=False).head(5)

# Merge to get the team colors for the top 5 riders
top_5_points_riders = top_5_points_riders.merge(race_data[['Rider', 'Team_Color']], on='Rider', how='left').drop_duplicates()

# Drop the Team_Color column before printing the table
top_5_points_riders_display = top_5_points_riders.drop(columns=['Team_Color'])

# Print the table without Team_Color
print("\nTop 5 Riders by Total Points in Race:")
print(top_5_points_riders_display.to_markdown(index=False))

# Create a dictionary mapping each Rider to their corresponding Team_Color (for plotting)
rider_color_map = dict(zip(top_5_points_riders['Rider'], top_5_points_riders['Team_Color']))

# Plotting Top 5 Riders by Total Points in Race
plt.figure(figsize=(12, 8))
sns.barplot(
    x='pts',
    y='Rider',
    data=top_5_points_riders,
    palette=rider_color_map,  # Use the color map here
    dodge=False,
    legend=False
)
plt.title('Top 5 Riders by Total Points in Race', fontsize=16)
plt.xlabel('Total Points', fontsize=12)
plt.ylabel('Rider', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()


# Ensure 'pos.' column is numeric
race_data['pos.'] = pd.to_numeric(race_data['pos.'], errors='coerce')

# Check for any NaN values after conversion (which means invalid positions)
print(race_data['pos.'].isna().sum())

# Now filter riders who finished in positions 1, 2, 3, 4, or 5
top_positions_riders = race_data[race_data['pos.'].isin([1, 2, 3, 4, 5])]

# Check if the filtered data has any rows
if top_positions_riders.empty:
    print("No riders finished in positions 1 to 5.")
else:
    # Count the occurrences of each rider in the top positions
    top_positions_counts = top_positions_riders.groupby('Rider')['pos.'].count().reset_index()
    top_positions_counts.columns = ['Rider', 'Count in Top 5']

    # Merge with team colors
    top_positions_counts = top_positions_counts.merge(race_data[['Rider', 'Team_Color']].drop_duplicates(), on='Rider', how='left')

    # Drop the Team_Color column before printing
    top_positions_counts_display = top_positions_counts.drop(columns=['Team_Color'])

    # Sort by the count in descending order and select the top 5 riders
    top_5_riders_by_top_positions = top_positions_counts_display.sort_values(by='Count in Top 5', ascending=False).head(5)

    # Print the table without Team_Color
    print("\nTop 5 Riders by Frequency of Finishing in Positions 1 to 5:")
    print(top_5_riders_by_top_positions.to_markdown(index=False))

    # Create a dictionary mapping each Rider to their corresponding Team_Color (for plotting)
    top_positions_color_map = dict(zip(top_positions_counts['Rider'], top_positions_counts['Team_Color']))

    # Plotting Top 5 Riders by Frequency of Finishing in Positions 1 to 5
    plt.figure(figsize=(12, 8))
    sns.barplot(
        x='Count in Top 5',
        y='Rider',
        data=top_5_riders_by_top_positions,
        palette=top_positions_color_map,  # Use the color map here
        dodge=False,
        legend=False
    )
    plt.title('Top 5 Riders by Frequency of Finishing in Positions 1 to 5', fontsize=16)
    plt.xlabel('Count of Top 5 Finishes', fontsize=12)
    plt.ylabel('Rider', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
plt.show()

"""# ***Data Visualisation Rider Finish Positions Every Race***

# ***Sprint***
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "/content/drive/MyDrive/UAS Datamin/dataset_motogp_updated.xlsx"
data = pd.ExcelFile(file_path)

# Check available sheet names
print("Available sheets:", data.sheet_names)

# Load the Sprint sheet explicitly
df = data.parse("Sprint")

# Clean column names for consistency (if necessary)
df.columns = df.columns.str.strip().str.lower()



# Add a new column for session name
df['session'] = 'spr'  # Adding a session column with the value 'spr'

# Extract unique events
events = df['event'].unique()

# Custom sort function for positions
def sort_positions(pos):
    if pos == 'DNF':
        return float('inf')
    return int(pos)

# Define team colors
team_colors = {
    "Ducati Lenovo Team": "#cc0101",
    "Prima Pramac Racing": "#8532c5",
    "Aprilia Racing": "#5bb33a",
    "Gresini Racing MotoGP": "#9fb2da",
    "CASTROL Honda LCR": "#dddddd",
    "IDEMITSU Honda LCR": "#dddddd",
    "Monster Energy Yamaha MotoGP Team": "#0b2d81",
    "Pertamina Enduro VR46 Racing Team": "#e1fa52",
    "Red Bull KTM Factory Racing": "#d55e2b",
    "Repsol Honda Team": "#fea111",
    "Red Bull GASGAS Tech3": "#990625",
    "Trackhouse Racing": "#0256ba"
}

# Plot each event
for event in events:
    # Filter data for the event
    event_data = df[df['event'] == event].copy()  # Avoid SettingWithCopyWarning

    # Sort by position with DNF last
    event_data['pos.'] = event_data['pos.'].apply(sort_positions)
    event_data = event_data.sort_values(by='pos.')

    # Ensure positions are sorted and consistent on the plot
    sorted_positions = [str(int(pos)) if pos != float('inf') else 'DNF' for pos in event_data['pos.']]

    # Assign colors based on team
    colors = [team_colors.get(team, "#000000") for team in event_data['team']]

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.barh(event_data['rider'], range(len(sorted_positions)), color=colors)
    plt.yticks(range(len(sorted_positions)), event_data['rider'])
    plt.xticks(range(len(sorted_positions)), sorted_positions)
    plt.xlabel('Pos. (Finish Position)')
    plt.ylabel('Nama Rider')
    plt.title(f'{event} - Finish Position Sprint')
    plt.gca().invert_yaxis()  # Optional: Invert y-axis for better readability

    # Show the plot
    plt.show()

"""# ***Race***

"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "/content/drive/MyDrive/UAS Datamin/dataset_motogp_updated.xlsx"
data = pd.ExcelFile(file_path)

# Check available sheet names
print("Available sheets:", data.sheet_names)

# Load the Sprint sheet explicitly
df = data.parse("Race")

# Clean column names for consistency (if necessary)
df.columns = df.columns.str.strip().str.lower()



# Add a new column for session name
df['session'] = 'rac'  # Adding a session column with the value 'spr'

# Extract unique events
events = df['event'].unique()

# Custom sort function for positions
def sort_positions(pos):
    if pos == 'DNF':
        return float('inf')
    return int(pos)

# Define team colors
team_colors = {
    "Ducati Lenovo Team": "#cc0101",
    "Prima Pramac Racing": "#8532c5",
    "Aprilia Racing": "#5bb33a",
    "Gresini Racing MotoGP": "#9fb2da",
    "CASTROL Honda LCR": "#dddddd",
    "IDEMITSU Honda LCR": "#dddddd",
    "Monster Energy Yamaha MotoGP Team": "#0b2d81",
    "Pertamina Enduro VR46 Racing Team": "#e1fa52",
    "Red Bull KTM Factory Racing": "#d55e2b",
    "Repsol Honda Team": "#fea111",
    "Red Bull GASGAS Tech3": "#990625",
    "Trackhouse Racing": "#0256ba"
}

# Plot each event
for event in events:
    # Filter data for the event
    event_data = df[df['event'] == event].copy()  # Avoid SettingWithCopyWarning

    # Sort by position with DNF last
    event_data['pos.'] = event_data['pos.'].apply(sort_positions)
    event_data = event_data.sort_values(by='pos.')

    # Ensure positions are sorted and consistent on the plot
    sorted_positions = [str(int(pos)) if pos != float('inf') else 'DNF' for pos in event_data['pos.']]

    # Assign colors based on team
    colors = [team_colors.get(team, "#000000") for team in event_data['team']]

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.barh(event_data['rider'], range(len(sorted_positions)), color=colors)
    plt.yticks(range(len(sorted_positions)), event_data['rider'])
    plt.xticks(range(len(sorted_positions)), sorted_positions)
    plt.xlabel('Pos. (Finish Position)')
    plt.ylabel('Nama Rider')
    plt.title(f'{event} - Finish Position Race')
    plt.gca().invert_yaxis()  # Optional: Invert y-axis for better readability

    # Show the plot
    plt.show()

"""# ***Klasifikasi***"""

# prompt: klasifikasi sprintnya

import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from Excel (assuming the file path is correct)
file_path = '/content/drive/MyDrive/UAS Datamin/dataset_motogp_updated.xlsx'
df_sprint = pd.read_excel(file_path, sheet_name='Sprint')
df_race = pd.read_excel(file_path, sheet_name='Race')


# Function to classify rider performance
def classify_performance(points):
    if points >= 25 :
        return "Excellent"
    elif points >= 15:
        return "Good"
    elif points >= 5:
        return "Fair"
    else:
        return "Poor"


# Apply classification to sprint and race data
df_sprint['Classification'] = df_sprint['pts'].apply(classify_performance)
df_race['Classification'] = df_race['pts'].apply(classify_performance)


# Display the updated tables with classification
print("Tabel Sprint Setelah Diklasifikasi:")
display(df_sprint)

print("Tabel Race Setelah Diklasifikasi:")
display(df_race)


# Example visualization of the classification (you can customize this further)
plt.figure(figsize=(12, 6))
sns.countplot(x='Classification', data=df_sprint, palette="viridis")
plt.title('Classification of Rider Performance in Sprint')
plt.xlabel('Performance Classification')
plt.ylabel('Number of Riders')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Classification', data=df_race, palette="viridis")
plt.title('Classification of Rider Performance in Race')
plt.xlabel('Performance Classification')
plt.ylabel('Number of Riders')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

# Load dataset
file_path = '/content/drive/MyDrive/UAS Datamin/dataset_motogp_updated.xlsx'  # Adjust the file path

data = pd.ExcelFile(file_path)

# Load sheets
sprint = data.parse('Sprint')
race = data.parse('Race')

# Combine Sprint and Race data
combined_data = pd.concat([sprint, race], ignore_index=True)

# Features and target
X = combined_data[['pos.', 'pts', 'session', 'year']]  # Features
y = combined_data['Rider']  # Target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Preprocessing for categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['pos.', 'session']),  # Encoding categorical columns
        ('num', StandardScaler(), ['pts', 'year'])  # Scaling numerical columns
    ]
)

# Pipeline with model
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', DecisionTreeClassifier(random_state=42))
])

# Parameter grid for hyperparameter tuning
param_grid = {
    'model__criterion': ['gini', 'entropy'],  # Impurity function
    'model__max_depth': [None, 5, 10, 15, 20, 30],  # Tree depth
    'model__min_samples_split': [2, 5, 10, 20],  # Minimum split
    'model__min_samples_leaf': [1, 2, 5, 10],  # Minimum leaf
    'model__splitter': ['best', 'random']  # Splitter type
}

# Grid Search for best parameters
grid_search = GridSearchCV(
    pipeline, param_grid, cv=5, scoring='accuracy', verbose=2, n_jobs=-1
)

# Train model with Grid Search
grid_search.fit(X_train, y_train)

# Display best parameters
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Accuracy and classification report
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)

# Convert classification report to DataFrame for better display
report_df = pd.DataFrame(report).transpose()

# Confusion Matrix
plt.figure(figsize=(10, 8))
disp = ConfusionMatrixDisplay.from_estimator(best_model, X_test, y_test, cmap='Blues', values_format='d')
plt.title('Confusion Matrix', fontsize=16)
plt.show()

# Print results in tables
print("\nBest Parameters:")
print(pd.DataFrame([best_params]))

print("\nAccuracy with Best Parameters:", accuracy)

print("\nClassification Report:")
print(report_df)

# Visualize classification report as a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(report_df.iloc[:-1, :-1], annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Classification Report Heatmap', fontsize=16)
plt.show()

"""# ***2025 MotoGP World Champion Prediction***"""

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

import warnings

# Disable warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Load data
file_path = '/content/dataset_motogp_updated.xlsx'  # Path file Anda
data = pd.ExcelFile(file_path)

# Load sheets
race_data = data.parse('Race')
lineup_2025 = data.parse('Line Up 2025')

# Filter data for the year 2024
season_2024 = race_data[race_data['year'] == 2024]

# Bersihkan kolom `pos.`
season_2024['pos.'] = pd.to_numeric(season_2024['pos.'], errors='coerce')
season_2024['pos.'] = season_2024['pos.'].fillna(25)  # Perbaikan tanpa inplace

# Aggregate data per rider for 2024
rider_stats_2024 = season_2024.groupby('Rider').agg({
    'pts': 'sum',      # Total points
    'pos.': 'mean',    # Average position
    'session': 'count' # Total sessions completed
}).reset_index()

# Filter riders based on 2025 lineup
riders_2025 = lineup_2025['Rider'].unique()
rider_stats_2024 = rider_stats_2024[rider_stats_2024['Rider'].isin(riders_2025)]

# Add team and color information from 2025 lineup
rider_stats_2024 = pd.merge(rider_stats_2024, lineup_2025[['Rider', 'Team']], on='Rider', how='left')

# Team Colors
default_color = "#808080"
team_colors = {
    "Ducati Lenovo Team": "#cc0101",
    "Prima Pramac Racing": "#8532c5",
    "Aprilia Racing": "#5bb33a",
    "Gresini Racing MotoGP": "#9fb2da",
    "CASTROL Honda LCR": "#dddddd",
    "IDEMITSU Honda LCR": "#dddddd",
    "Monster Energy Yamaha MotoGP Team": "#0b2d81",
    "Pertamina Enduro VR46 Racing Team": "#e1fa52",
    "Red Bull KTM Factory Racing": "#fd6500",
    "Repsol Honda Team": "#fea111",
    "Red Bull KTM Tech3": "#fa6400",
    "Trackhouse Racing": "#0256ba",
    "Pertamina Enduro VR46 MotoGP Team": "#e1fa52",
    "Yamaha Factory Racing Team": "#0b2d81",
    "HRC Test Team": "#dddddd"
}

# Fungsi pencocokan nama tim
def match_team_name(team_name, team_colors):
    match = process.extractOne(team_name, team_colors.keys())
    if match and match[1] >= 80:  # Ambang kecocokan 80%
        return match[0]
    return None  # Jika tidak ada kecocokan, gunakan warna default

# Assign colors to teams using fuzzy matching
rider_stats_2024['Team Color'] = rider_stats_2024['Team'].apply(
    lambda x: team_colors.get(match_team_name(x, team_colors), default_color)
)

# Define the target
rider_stats_2024['Champion'] = (rider_stats_2024['pts'] == rider_stats_2024['pts'].max()).astype(int)

# Features and target
X = rider_stats_2024[['pts', 'pos.', 'session']]  # Features
y = rider_stats_2024['Champion']  # Target

# Train-test split (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model: Decision Tree (CART)
model = DecisionTreeClassifier(random_state=42)

# Hyperparameter tuning with GridSearchCV
param_grid = {
    'criterion': ['gini', 'entropy'],  # Split criterion
    'max_depth': [3, 5, 10, None],     # Max depth
    'min_samples_split': [2, 5, 10],  # Minimum samples to split
    'min_samples_leaf': [1, 2, 5]     # Minimum samples in a leaf node
}

grid_search = GridSearchCV(model, param_grid, cv=3, scoring='accuracy', verbose=0, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Best parameters
best_model = grid_search.best_estimator_
best_params = pd.DataFrame([grid_search.best_params_])
print("\nBest Parameters:\n", best_params)

# Evaluate on test set
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred, output_dict=True)
classification_df = pd.DataFrame(classification_rep).transpose()
print("\nAccuracy:", accuracy)
print("\nClassification Report:\n", classification_df)

# Predict champion for 2025
future_data = rider_stats_2024.copy()  # Assume 2024 stats predict 2025
future_data['Prediction'] = best_model.predict(future_data[['pts', 'pos.', 'session']])

# Predicted champion
predicted_champion = future_data[future_data['Prediction'] == 1]

# Tampilkan hasil prediksi dalam bentuk tabel
predicted_champion_table = predicted_champion[['Rider', 'pts', 'pos.', 'session', 'Team']]
print("\nPredicted Champion for 2025:\n")
print(predicted_champion_table.to_markdown(index=False))

# Visualize comparison
plt.figure(figsize=(14, 8))

sns.barplot(
    data=future_data.sort_values(by='pts', ascending=False),  # Sort by points
    x='Rider',  # Riders on x-axis
    y='pts',  # Points on y-axis
    hue='Team',  # Team as hue
    palette=dict(zip(future_data['Team'], future_data['Team Color']))  # Map teams to colors
)

plt.title("Comparison of Predicted Points for MotoGP 2025", fontsize=16)
plt.ylabel("Points", fontsize=12)
plt.xlabel("Riders", fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for clarity
plt.legend(title='Teams')
plt.tight_layout()
plt.show()

# Team Colors
default_color = "#808080"
team_colors = {
    "Ducati Lenovo Team": "#cc0101",
    "Prima Pramac Racing": "#8532c5",
    "Aprilia Racing": "#5bb33a",
    "Gresini Racing MotoGP": "#9fb2da",
    "CASTROL Honda LCR": "#dddddd",
    "IDEMITSU Honda LCR": "#dddddd",
    "Monster Energy Yamaha MotoGP Team": "#0b2d81",
    "Pertamina Enduro VR46 Racing Team": "#e1fa52",
    "Red Bull KTM Factory Racing": "fd6500",
    "Repsol Honda Team": "#fea111",
    "Red Bull KTM Tech3": "#fa6400",
    "Trackhouse Racing": "#0256ba",
    "Pertamina Enduro VR46 MotoGP Team": "#e1fa52",
    "Yamaha Factory Racing Team": "#0b2d81",
    "HRC Test Team": "#dddddd"
}

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from rapidfuzz import process
import warnings

# Disable warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Load data
file_path = '/content/dataset_motogp_updated.xlsx'  # Path file Anda
data = pd.ExcelFile(file_path)

# Load sheets
race_data = data.parse('Race')
lineup_2025 = data.parse('Line Up 2025')

# Filter data for the year 2024
season_2024 = race_data[race_data['year'] == 2024]

# Bersihkan kolom `pos.`
season_2024['pos.'] = pd.to_numeric(season_2024['pos.'], errors='coerce')
season_2024['pos.'] = season_2024['pos.'].fillna(25)  # Perbaikan tanpa inplace

# Aggregate data per rider for 2024
rider_stats_2024 = season_2024.groupby('Rider').agg({
    'pts': 'sum',      # Total points
    'pos.': 'mean',    # Average position
    'session': 'count' # Total sessions completed
}).reset_index()

# Filter riders based on 2025 lineup
riders_2025 = lineup_2025['Rider'].unique()
rider_stats_2024 = rider_stats_2024[rider_stats_2024['Rider'].isin(riders_2025)]

# Add team and color information from 2025 lineup
rider_stats_2024 = pd.merge(rider_stats_2024, lineup_2025[['Rider', 'Team']], on='Rider', how='left')

# Team Colors
default_color = "#808080"
team_colors = {
    "Ducati Lenovo Team": "#cc0101",
    "Prima Pramac Racing": "#8532c5",
    "Aprilia Racing": "#5bb33a",
    "Gresini Racing MotoGP": "#9fb2da",
    "CASTROL Honda LCR": "#dddddd",
    "IDEMITSU Honda LCR": "#dddddd",
    "Monster Energy Yamaha MotoGP Team": "#0b2d81",
    "Pertamina Enduro VR46 Racing Team": "#e1fa52",
    "Red Bull KTM Factory Racing": "#fd6500",
    "Repsol Honda Team": "#fea111",
    "Red Bull KTM Tech3": "#fa6400",
    "Trackhouse Racing": "#0256ba",
    "Pertamina Enduro VR46 MotoGP Team": "#e1fa52",
    "Yamaha Factory Racing Team": "#0b2d81",
    "HRC Test Team": "#dddddd"
}

# Fungsi pencocokan nama tim
def match_team_name(team_name, team_colors):
    match = process.extractOne(team_name, team_colors.keys())
    if match and match[1] >= 80:  # Ambang kecocokan 80%
        return match[0]
    return None  # Jika tidak ada kecocokan, gunakan warna default

# Assign colors to teams using fuzzy matching
rider_stats_2024['Team Color'] = rider_stats_2024['Team'].apply(
    lambda x: team_colors.get(match_team_name(x, team_colors), default_color)
)

# Define the target
rider_stats_2024['Champion'] = (rider_stats_2024['pts'] == rider_stats_2024['pts'].max()).astype(int)

# Features and target
X = rider_stats_2024[['pts', 'pos.', 'session']]  # Features
y = rider_stats_2024['Champion']  # Target

# Train-test split (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model: Decision Tree (CART)
model = DecisionTreeClassifier(random_state=42)

# Hyperparameter tuning with GridSearchCV
param_grid = {
    'criterion': ['gini', 'entropy'],  # Split criterion
    'max_depth': [3, 5, 10, None],     # Max depth
    'min_samples_split': [2, 5, 10],  # Minimum samples to split
    'min_samples_leaf': [1, 2, 5]     # Minimum samples in a leaf node
}

grid_search = GridSearchCV(model, param_grid, cv=3, scoring='accuracy', verbose=0, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Best parameters
best_model = grid_search.best_estimator_
best_params = pd.DataFrame([grid_search.best_params_])
print("\nBest Parameters:\n", best_params)

# Evaluate on test set
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred, output_dict=True)
classification_df = pd.DataFrame(classification_rep).transpose()
print("\nAccuracy:", accuracy)
print("\nClassification Report:\n", classification_df)

# Predict champion for 2025
future_data = rider_stats_2024.copy()  # Assume 2024 stats predict 2025
future_data['Prediction'] = best_model.predict(future_data[['pts', 'pos.', 'session']])

# Predicted champion
predicted_champion = future_data[future_data['Prediction'] == 1]
print("\nPredicted Champion for 2025:\n", predicted_champion[['Rider', 'pts', 'pos.', 'session', 'Team']])

# Tampilkan hasil prediksi dalam bentuk tabel
predicted_champion_table = predicted_champion[['Rider', 'pts', 'pos.', 'session', 'Team']]
print("\nPredicted Champion for 2025 (Formatted):\n")
print(predicted_champion_table.to_markdown(index=False))

# Visualize comparison
plt.figure(figsize=(14, 8))

sns.barplot(
    data=future_data.sort_values(by='pts', ascending=False),  # Sort by points
    x='Rider',  # Riders on x-axis
    y='pts',  # Points on y-axis
    hue='Team',  # Team as hue
    palette=dict(zip(future_data['Team'], future_data['Team Color']))  # Map teams to colors
)

plt.title("Comparison of Predicted Points for MotoGP 2025", fontsize=16)
plt.ylabel("Points", fontsize=12)
plt.xlabel("Riders", fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for clarity
plt.legend(title='Teams')
plt.tight_layout()
plt.show()
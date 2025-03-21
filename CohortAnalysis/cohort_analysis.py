import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

# ================================
# Data Loading Section
# ================================
# Load the data from the provided URL
df = pd.read_csv('https://raw.githubusercontent.com/avkotova/MyPythonSketches/a0fab1ba99f4f0277ed6f1d9e78919e69b10c752/CohortAnalysis/mock_data.csv')

# ================================
# Data Preprocessing Section
# ================================
# Convert 'created_at' column to datetime format
df['created_at'] = pd.to_datetime(df['created_at'])

# Calculate the first contact date for each client based on 'extra_leads'
df['first_dt'] = df.groupby('extra_leads')['created_at'].transform('min')

# Create 'first_ym' and 'ym' columns to store the year-month format
df['first_ym'] = df['first_dt'].dt.strftime('%Y-%m')
df['ym'] = df['created_at'].dt.strftime('%Y-%m')

# ================================
# Cohort Analysis Section
# ================================
# Create a pivot table for cohort analysis
cohorts = pd.pivot_table(
    df,
    index='first_ym',  # Rows represent the first contact month for the cohort
    columns='ym',  # Columns represent the subsequent months
    values='extra_leads',
    aggfunc='nunique'  # Count unique clients
).fillna(0)

# ================================
# Data Normalization Section
# ================================
# Normalize the cohort data by the first row to get percentages
diags = np.diag(cohorts)  # Get diagonal values (first values in each cohort row)
cohorts_percentage = cohorts.div(diags, axis=0)  # Normalize the data for percentages

# ================================
# Visualization Setup Section
# ================================
# Set up a custom color palette from light blue to soft green
cmap = mcolors.LinearSegmentedColormap.from_list(
    "light_blue_to_soft_green", ["#ADD8E6", "#228B22"], N=256
)

# Create the figure with two subplots (for two heatmaps)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 10))  # One row, two columns for the graphs

# ================================
# Plotting Section
# ================================
# First heatmap (left graph) - showing percentage values
sns.heatmap(
    cohorts_percentage,
    annot=True,
    fmt='.0%',  # Display percentages
    linewidths=0.5,
    vmin=0.4,
    vmax=np.percentile(cohorts_percentage, 90),  # Limit color range to 90th percentile
    cmap=cmap,  # Use the custom color palette
    cbar=False,  # Hide color bar
    square=True,
    annot_kws={'size': 10, 'weight': 'normal', 'color': 'white'},  # Smaller text and normal font weight
    ax=ax1
)

# Second heatmap (right graph) - showing the absolute values (users)
sns.heatmap(
    cohorts_percentage,
    annot=False,  # Remove percentage annotations
    linewidths=0.5,
    vmin=0.4,
    vmax=np.percentile(cohorts_percentage, 90),  # Same color range as first heatmap
    cmap=cmap,  # Same color palette
    cbar=False,  # Hide color bar
    square=True,
    ax=ax2
)

# ================================
# Annotation Section
# ================================
# Add absolute values on top of percentages in the second heatmap
for i in range(len(cohorts)):
    for j in range(len(cohorts.columns)):
        ax2.text(
            j + 0.5,  # Position along the X-axis (shift to center)
            i + 0.5,  # Position along the Y-axis (shift to center)
            int(cohorts.iloc[i, j]),  # Display the absolute value
            ha='center', va='center', color='white', fontsize=10, weight='normal'
        )

# ================================
# Final Adjustments Section
# ================================
# Set titles for the plots
ax1.set_title("Cohort Analysis (%)")  # Left graph shows percentages
ax2.set_title("Cohort Analysis (Users)")  # Right graph shows absolute number of users

# Set X-axis labels at the top of both graphs
ax1.xaxis.set_label_position('top')
ax1.xaxis.tick_top()
ax2.xaxis.set_label_position('top')
ax2.xaxis.tick_top()

# Remove axis labels (like 'first_ym' and 'ym') on both graphs
ax1.set_xlabel('')  # Remove X-axis label on the first graph
ax1.set_ylabel('')  # Remove Y-axis label on the first graph
ax2.set_ylabel('')  # Remove Y-axis label on the second graph

# Rotate the X-axis labels for better readability
ax1.tick_params(axis='x', rotation=45)
ax2.tick_params(axis='x', rotation=45)

# ================================
# Show the Plot
# ================================
# Display the graphs
plt.tight_layout()  # Adjust layout for better spacing
plt.show()  # Show the figure

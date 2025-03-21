# Cohort Analysis for Parent Portal Engagement

## Objective  
This project analyzes parent engagement with an online school’s parent portal, which provides articles, webinars, and tips on child psychology. The goal was to evaluate the effectiveness of monthly webinars and identify which topics generate the most interest among parents.

## Problem
The school runs webinars every month to engage parents, but the success rate varies significantly. We wanted to measure engagement based on the subscription month of parents to understand which topics perform best.

## Solution
To analyze engagement, I created a cohort heatmap to visualize the relationship between the parent subscription month and the engagement level with webinars. The heatmap shows both the percentage of active participants and the absolute number of views per webinar, making it easy to identify patterns and trends in the data.

### Key Steps:
1. **Data Collection**: Gathered data on parent subscriptions and their interactions with webinars.
2. **Data Processing**: Normalized the data for cohort analysis and calculated percentages.
3. **Visualization**: Created a heatmap using Python's `seaborn` and `matplotlib` libraries to represent the cohort analysis visually.
4. **Insights**: Identified which webinar topics were most engaging, helping optimize future marketing strategies.

## How to Use
- **Data Input**: Replace the sample data with actual data from the parent portal system.
- **Visualization**: Run the provided Python scripts to generate cohort analysis heatmaps.
- **CRM Integration**: This analysis can be easily integrated into CRM tools to provide managers with real-time insights on webinar performance.

## Files:
- `cohort_analysis.py` – Python script for cohort analysis.
- `heatmap_visualization.py` – Script to generate the heatmap visualization.
- `mock_data.csv` – Example dataset for testing.

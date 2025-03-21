# Cohort Analysis for Parent Portal Engagement  

## Objective  
This project analyzes parent engagement with an online school’s parent portal, which provides articles, webinars, and tips on child psychology. The goal is to evaluate the effectiveness of monthly webinars and identify which topics generate the most interest among parents.  

## Problem  
The school runs webinars every month to engage parents, but engagement levels vary significantly. We needed to analyze how engagement changes over time, based on when parents subscribed.  

## Solution  
I built a cohort heatmap to visualize the relationship between the parent subscription month and engagement with webinars. The heatmap shows:  
- Percentage of engaged parents per cohort  
- Absolute number of views per webinar (overlaid on the same heatmap for clarity)  

This helps easily spot trends and optimize marketing efforts.  

### Key Steps  
- Data Collection: Gathered parent subscription and webinar interaction data.  
- Data Processing: Normalized data and calculated engagement percentages.  
- Visualization: Created a cohort heatmap using Python (Seaborn, Matplotlib).
- CRM Integration: Use results to track engagement in real time.  
- Insights: Identified top-performing webinar topics to improve future marketing.  


## Files  
- `cohort_analysis.py` – Python script for data processing and visualization.  
- `mock_data.csv` – Sample dataset for testing.  
- `cohort_analysis_result.png` – Example of the generated heatmap.  

## Visualization  
The cohort analysis results in the following heatmaps:  

- The percentage-based heatmap shows the retention rate of parents per cohort.  
- The absolute values (number of engaged parents) are overlaid on the same heatmap for better clarity, ensuring both relative and absolute engagement trends are visible in a single view.  

![Cohort Analysis Result](CohortAnalysis/cohort_analysis_result.png)  

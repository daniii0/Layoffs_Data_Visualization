# DATA WEEK PROJECT

import pandas as pd
import matplotlib.pyplot as plt
 
# 1. Load the dataset
df = pd.read_csv('layoffs.csv')

# 2. Display the first few rows
print("Preview of data:")
print(df.head())

# 3. Check basic info
print("\nDataset info:")
print(df.info())

# 4. Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# 5. Drop rows with no total_laid_off value
df_clean = df.dropna(subset=['total_laid_off'])

# 6. Basic stats
print("\nNumber of rows after cleaning:", len(df_clean))
print("Date range:", df_clean['date'].min(), "to", df_clean['date'].max())
print("Top 5 companies with highest layoffs:")
print(df_clean.groupby('company')['total_laid_off'].sum().sort_values(ascending=False).head())


# 7. Top 10 companies with highest layoffs
top10 = df_clean.groupby('company')['total_laid_off'].sum().sort_values(ascending=False).head(10)

# 8. Create a monthly layoffs trend over time
df_clean['month'] = df_clean['date'].dt.to_period('M')  # convert to month period
monthly_trend = df_clean.groupby('month')['total_laid_off'].sum()



import os

# Create folder to save plots
os.makedirs('plots', exist_ok=True)

# 9. Layoffs by Industry (top 8 industries)
industry_totals = df_clean.groupby('industry')['total_laid_off'].sum().sort_values(ascending=False).head(8)

plt.figure(figsize=(10,6))
industry_totals.plot(kind='bar')
plt.title('Top Industries by Total Tech Layoffs')
plt.xlabel('Industry')
plt.ylabel('Total Employees Laid Off')
plt.tight_layout()
plt.savefig('plots/layoffs_by_industry.png')
plt.show()

# Re-save previous plots too
# (Top 10 companies plot)
plt.figure(figsize=(10,6))
top10.sort_values().plot(kind='barh')
plt.title('Top 10 Companies by Total Tech Layoffs')
plt.xlabel('Total Employees Laid Off')
plt.ylabel('Company')
plt.tight_layout()
plt.savefig('plots/top_companies.png')
plt.show()

# (Monthly trend plot)
plt.figure(figsize=(12,6))
monthly_trend.plot()
plt.title('Total Tech Layoffs per Month (2020–2023)')
plt.xlabel('Month')
plt.ylabel('Total Employees Laid Off')
plt.tight_layout()
plt.savefig('plots/monthly_trend.png')
plt.show()

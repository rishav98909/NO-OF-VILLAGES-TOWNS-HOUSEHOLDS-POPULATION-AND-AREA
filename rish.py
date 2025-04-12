import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Load and inspect the dataset 
df = pd.read_excel(r"C:\Users\Rishav kumar\Downloads\A-1_NO_OF_VILLAGES_TOWNS_HOUSEHOLDS_POPULATION_AND_AREA.xlsx", skiprows=5)

# Rename the columns properly
df.columns = [
    "State_Code", "District_Code", "Subdistrict_Code", "Area_Name", "Area_Type",
    "Rural_Urban", "No_of_Villages", "No_of_Towns", "Uninhabited_Villages",
    "Households", "Population_Total", "Population_Male", "Population_Female",
    "Area_sq_km", "Density_per_sqkm"
]

# Drop any rows with all NaNs
df.dropna(how='all', inplace=True)

# Convert numerical columns to proper dtypes
numeric_cols = [
    'No_of_Villages', 'No_of_Towns', 'Uninhabited_Villages', 'Households',
    'Population_Total', 'Population_Male', 'Population_Female',
    'Area_sq_km', 'Density_per_sqkm'
]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Fill missing values with 0 or 'Unknown' as appropriate
df.fillna({
    'No_of_Villages': 0,
    'No_of_Towns': 0,
    'Uninhabited_Villages': 0,
    'Households': 0,
    'Population_Total': 0,
    'Population_Male': 0,
    'Population_Female': 0,
    'Area_sq_km': 0,
    'Density_per_sqkm': 0,
    'Area_Name': 'Unknown',
    'Area_Type': 'Unknown',
    'Rural_Urban': 'Unknown'
}, inplace=True)

# Show basic statistics
print("Basic Statistics:")
print(df.describe())

# (a) Histogram – Distribution of Area in sq.km
plt.figure(figsize=(8, 4))
sb.histplot(df['Area_sq_km'], bins=20, kde=True, color='skyblue')
plt.title("Distribution of Area (sq. km)")
plt.xlabel("Area (sq. km)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# (b) Pie Chart – Urban vs Rural Area Count
area_type_counts = df['Rural_Urban'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(area_type_counts, labels=area_type_counts.index, autopct='%1.1f%%', startangle=90, colors=sb.color_palette('pastel'))
plt.title("Distribution of Area Type (Urban vs Rural)")
plt.axis('equal')
plt.tight_layout()
plt.show()

# (c) Scatter Plot – Households vs Population Total
plt.figure(figsize=(8, 5))
sb.scatterplot(data=df, x='Households', y='Population_Total', hue='Rural_Urban', palette='coolwarm')
plt.title("Households vs Total Population")
plt.xlabel("Number of Households")
plt.ylabel("Total Population")
plt.tight_layout()
plt.show()

# (d) Line Plot – Top 10 Densely Populated Areas
top_density = df.sort_values(by='Density_per_sqkm', ascending=False).head(10)
plt.figure(figsize=(10, 5))
sb.lineplot(data=top_density, x='Area_Name', y='Density_per_sqkm', marker='o', color='green')
plt.title("Top 10 Areas by Population Density")
plt.xticks(rotation=45)
plt.ylabel("Density per sq.km")
plt.tight_layout()
plt.show()

# (e) Bar Plot – Top 10 Areas by Total Population
top_population = df.sort_values(by='Population_Total', ascending=False).head(10)
plt.figure(figsize=(10, 5))
sb.barplot(data=top_population, x='Area_Name', y='Population_Total', hue='Area_Name', palette='magma', legend=False)
plt.title("Top 10 Areas by Total Population")
plt.xlabel("Area")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# (f) Heatmap – Correlation Matrix of Numerical Columns
correlation_data = df[numeric_cols].corr()
plt.figure(figsize=(8, 6))
sb.heatmap(correlation_data, annot=True, cmap='coolwarm', linewidths=0.5, square=True)
plt.title("Correlation Heatmap of Village Data")
plt.tight_layout()
plt.show()

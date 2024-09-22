import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the correct path
df = pd.read_csv('C:/Users/HP/Desktop/ECM/mtcars.csv')  # Adjust the path to where your file is located

# Plot the histogram for 'mpg'
plt.figure(figsize=(8,6))
plt.hist(df['mpg'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of MPG (Miles per Gallon)')
plt.xlabel('Miles per Gallon (MPG)')
plt.ylabel('Frequency')

plt.show()

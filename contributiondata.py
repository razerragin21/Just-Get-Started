import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('data.csv')

# Transpose the DataFrame to swap the x and y axes
df_transposed = df.T

# Create a heatmap using the 'seaborn' library
sns.heatmap(df_transposed, xticklabels=True, yticklabels=True)

# Draw a grid on the plot
plt.grid(True, linewidth=0.5)

# Set the size of the plot
plt.figure(figsize=(10,5))

# Add spacing between the rows
plt.subplots_adjust(hspace=0.5)

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {"Barton Springs Car Wash": 125.75 , "Juliet Italian Kitchen": 133.6 , "Austin Collective Dispensary": 105.99, \
        "Lou's Barton Springs": 137.49, "Cannone Gelato": 169.91, "Baby Acapulco's": 89.6, "That Food Truck": 245.36, \
        "Green Mesquite BBQ": 58.46, "Barton Springs Bike Rental": 34.57, "Barton Brisk Corner Chevron": 106.54, \
        "Juiceland": 93.52, "Pav Bhaji Express": 27.14}
df = pd.DataFrame(list(data.items()), columns=['Business', 'Waste'])
df['Business'] = df['Business'].str.replace(' ', '\n')
plt.figure(figsize=(10, 8))
bar_width = 0.4
bar_positions = np.arange(len(df)) * (bar_width + 2.7)
plt.bar(df['Business'], df['Waste'], color='skyblue')
plt.xlabel("Business", fontsize=12)
plt.ylabel('Waste Collected (Lbs)', fontsize=12)
plt.title("Total Waste Park Watch Inc. Collected by Bin Over Summer '24", fontsize=14)
for index, value in enumerate(df['Waste']):
    plt.text(index, value + 6, str(value), ha='center')

plt.ylim(0, max(df['Waste']) + 50) 
plt.tight_layout()
plt.show()

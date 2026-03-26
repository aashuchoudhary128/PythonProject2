import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'month': [1,2,3,4,5,6,7,8,9,10,11,12],
    'facecream': [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    'facewash': [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
}

df = pd.DataFrame(data)

months = df['month']
x = np.arange(len(months))

plt.bar(x - 0.2, df['facecream'], width=0.4, label='Face Cream')
plt.bar(x + 0.2, df['facewash'], width=0.4, label='Face Wash')

plt.xticks(x, months)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Face Cream vs Face Wash Sales')

plt.legend()
plt.show()
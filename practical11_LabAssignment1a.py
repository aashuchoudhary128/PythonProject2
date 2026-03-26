import pandas as pd
import matplotlib.pyplot as plt

data = {
    'month': [1,2,3,4,5,6,7,8,9,10,11,12],
    'total_profit': [211000,183300,224700,229000,228000,210000,
                     200000,260000,234000,266000,300000,310000]
}

df = pd.DataFrame(data)

plt.plot(df['month'], df['total_profit'], marker='o')

plt.title('Total Profit per Month')
plt.xlabel('Month')
plt.ylabel('Profit')

plt.grid()
plt.show()
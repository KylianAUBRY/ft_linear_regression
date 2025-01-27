import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')  # usecols=['price']
ax = data.plot(kind="scatter", x="km", y ="price")


print(data)
# plt.plot(data)
plt.show()
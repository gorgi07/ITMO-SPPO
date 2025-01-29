import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataFrame = pd.read_csv('lab5_3.csv', sep=';')
dataFrame['<OPEN>'] = pd.to_numeric(dataFrame['<OPEN>'])
dataFrame['<HIGH>'] = pd.to_numeric(dataFrame['<HIGH>'])
dataFrame['<LOW>'] = pd.to_numeric(dataFrame['<LOW>'])
dataFrame['<CLOSE>'] = pd.to_numeric(dataFrame['<CLOSE>'])
dataFrame = pd.melt(dataFrame, id_vars=['<DATE>'], value_vars=['<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>'])
sns.boxplot(x='<DATE>',
            y='value',
            data=dataFrame,
            hue='variable',
            showmeans=True,
            meanprops={"marker": "x", "markeredgecolor": "black", "markersize": 5}
            )
plt.title("Ящик с усами (Француз???)")
plt.legend()
plt.show()

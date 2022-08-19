import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('titanic_dataset.csv')
print(df)
df.info()
df.isnull().sum()
df.duplicated().sum()
# categorial data
sns.countplot(df['Sex'])
sns.show()

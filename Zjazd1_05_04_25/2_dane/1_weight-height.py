import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('weight-height.csv', sep=';')
print(df)
print(type(df))

print(df.Gender.value_counts())

df.Height *= 2.54
df.Weight /= 2.2

df['nowa'] = (df.Height + 6) / df.Weight
print(df.head(10))

plt.hist(df.query("Gender=='Male'").Weight, bins=30)
# plt.show()
plt.hist(df.query("Gender=='Female'").Weight, bins=30)
plt.show()
sns.histplot(df.query("Gender=='Male'").Weight, bins=30)
# plt.show()
sns.histplot(df.query("Gender=='Female'").Weight, bins=30)
plt.show()

del (df['nowa'])

df = pd.get_dummies(df)

del (df['Gender_Male'])
df = df.rename(columns={'Gender_Female': 'Gender'})
print(df)

df.to_csv('waga_wzrost_po_edycji.csv')




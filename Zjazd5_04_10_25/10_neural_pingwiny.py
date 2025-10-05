import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
# print(type(penguins))
print(penguins.head().to_string())

# sns.pairplot(penguins, hue='species')
# plt.show()

penguins_filtered = penguins.drop(columns=['island', 'sex']).dropna()
penguins_features = penguins_filtered.drop(columns=['species'])
penguins_target = pd.get_dummies(penguins_filtered['species'])
print(penguins_target)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(penguins_features, penguins_target, test_size=0.2)

from tensorflow import keras
inputs = keras.Input(shape=[X_train.shape[1]])
hidden_layer1 = keras.layers.Dense(5, activation='relu')(inputs)
hidden_layer2 = keras.layers.Dense(5, activation='relu')(hidden_layer1)
hidden_layer3 = keras.layers.Dense(5, activation='relu')(hidden_layer2)
output_layer = keras.layers.Dense(3, activation='softmax')(hidden_layer3)

model = keras.Model(inputs=inputs, outputs=output_layer)
model.compile(optimizer='adam', loss=keras.losses.CategoricalCrossentropy())
result = model.fit(X_train, y_train, epochs=100)
sns.lineplot(x=result.epoch, y=result.history['loss'])
plt.show()
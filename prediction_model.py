import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


troop_movements = pd.read_csv('troop_movements.csv')
empire_or_resistance_counts = troop_movements['empire_or_resistance'].value_counts()
homeworld_counts = troop_movements['homeworld'].value_counts()
unit_type_counts = troop_movements['unit_type'].value_counts()
troop_movements['is_resistance'] = troop_movements['empire_or_resistance'] == 'resistance'

sns.countplot(x='empire_or_resistance', data=troop_movements)
plt.title('Character Count by Empire or Resistance') 

x=troop_movements[['homeworld', 'unit_type']]
x_encoded=pd.get_dummies(x)
y=troop_movements['is_resistance']

X_train, X_test, Y_train, Y_test = train_test_split(x_encoded, y, test_size=0.3, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
accuracy = model.score(X_test, Y_test)

importances = model.feature_importances_
feature_importances = pd.DataFrame({'Feature': x_encoded.columns, 'Importance': importances})
feature_importances = feature_importances.sort_values(by='Importance', ascending=False)
plt.figure(figsize=(10,12))
sns.barplot(x='Feature', y='Importance', data=feature_importances)
plt.xticks(rotation=90)
plt.title('Feature Importances')
plt.show()

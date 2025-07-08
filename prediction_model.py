import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

troop_movements = pd.read_csv('troop_movements.csv')
empire_or_resistance_counts = troop_movements['empire_or_resistance'].value_counts()
homeworld_counts = troop_movements['homeworld'].value_counts()
unit_type_counts = troop_movements['unit_type'].value_counts()
troop_movements['is_resistance'] = troop_movements['empire_or_resistance'] == 'resistance'

sns.countplot(x='empire_or_resistance', data=troop_movements)
plt.title('Character Count by Empire or Resistance') 
plt.show() 

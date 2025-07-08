import pandas as pd

troop_movements = pd.read_csv('troop_movements.csv')
empire_or_resistance_counts = troop_movements['empire_or_resistance'].value_counts()
homeworld_counts = troop_movements['homeworld'].value_counts()
unit_type_counts = troop_movements['unit_type'].value_counts()
troop_movements['is_resistance'] = troop_movements['empire_or_resistance'] == 'resistance'



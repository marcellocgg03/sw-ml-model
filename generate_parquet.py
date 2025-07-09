import pandas as pd

troop_movements = pd.read_csv('troop_movements_1m.csv')
troop_movements['unit_type']=troop_movements['unit_type'].replace('invalid_unit', 'unkown')
troop_movements[['location_x', 'location_y']]=troop_movements[['location_x', 'location_y']].fillna(method='ffill')
troop_movements.to_parquet('troop_movements_1m.parquet', engine='pyarrow')
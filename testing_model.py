import pickle as pkl
import pandas as pd

with open('trained_model.pkl', 'rb') as f:
    model = pkl.load(f)

data=pd.read_parquet('troop_movements_1m.parquet')
x=data[['homeworld', 'unit_type']]
x_encoded=pd.get_dummies(x)
data['predictions'] = model.predict(x_encoded)
print(data.head())
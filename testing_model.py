import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import plot_tree
from sklearn import tree
from sklearn.tree import export_text

with open('trained_model.pkl', 'rb') as f:
    model = pkl.load(f)

data=pd.read_parquet('troop_movements_1m.parquet')
x=data[['homeworld', 'unit_type']]
x_encoded=pd.get_dummies(x)
data['predictions'] = model.predict(x_encoded)
text_tree = tree.export_text(model, feature_names=x_encoded.columns)
print(text_tree)

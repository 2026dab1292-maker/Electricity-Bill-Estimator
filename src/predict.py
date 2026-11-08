import pickle
import pandas as pd
from train_model import FEATURES
with open("outputs/model.pkl","rb") as file:
    model = pickle.load(file)

print("Enter the household details:")
values = []
for feature in FEATURES:
    values.append(float(input(feature + ": ")))


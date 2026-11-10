# main.py
# Written by: Member 2 (Execution lead)
# Job: run all steps one after another.
# Run from the main project folder:  python src/main.py

import os

from data_cleaning import load_and_clean
from eda import run_eda
from result_plots import make_result_plots
from train_model import train_and_evaluate

# Folder where all charts and results will be saved
os.makedirs("outputs", exist_ok=True)

print("Step 1: Load and clean data")
df = load_and_clean("data/household_energy_bill_data.csv")

print("Step 2: Explore data")
run_eda(df)

print("Step 3: Train and test model")
model, y_test, y_pred, r2 = train_and_evaluate(df)

print("Step 4: Make result charts")
make_result_plots(y_test, y_pred, r2)

print("Done! Check the outputs/ folder.")

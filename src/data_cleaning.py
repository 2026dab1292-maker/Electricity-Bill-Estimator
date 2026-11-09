# data_cleaning.py
# Written by: Member 1 (Documentation lead)
# Job: read the CSV file and remove wrong rows.

import pandas as pd


def load_and_clean(path):
    # Read the dataset
    df = pd.read_csv(path)
    print("Rows before cleaning:", len(df))

    # Remove empty and repeated rows
    df = df.dropna()
    df = df.drop_duplicates()

    # Remove rows that have impossible values
    df = df[df["num_rooms"] >= 0]
    df = df[df["num_people"] >= 1]
    df = df[df["num_children"] >= 0]
    df = df[df["housearea"] > 0]
    df = df[df["ave_monthly_inc"] >= 0]
    df = df[df["amount_paid"] > 0]

    # Yes/No columns must be only 0 or 1
    for column in ["is_ac", "is_tv", "is_flat", "is_urban"]:
        df = df[df[column].isin([0, 1])]

    print("Rows after cleaning:", len(df))
    return df

# Written by: Member 1 (Documentation lead)

import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path)
    print("Rows before cleaning:", len(df))

    df = df.dropna()
    df = df.drop_duplicates()

    df = df[df["num_rooms"] >= 0]
    df = df[df["num_people"] >= 1]
    df = df[df["num_children"] >= 0]
    df = df[df["housearea"] > 0]
    df = df[df["ave_monthly_income"] >= 0]
    df = df[df["amount_paid"] > 0]

    for column in ["is_ac", "is_tv", "is_flat", "is_urban"]:
        df = df[df[column].isin([0, 1])]

    print("Rows after cleaning:", len(df))
    return df

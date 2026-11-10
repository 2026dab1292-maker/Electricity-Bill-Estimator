#written by : ppt lead (2026EEB1361)
import pandas as pd
import matplotlib.pyplot as plt

def scatter_chart(df, column, filename):
    # Scatter plot of one column against the electricity bill
    plt.scatter(df[column], df["amount_paid"], alpha=0.5)
    plt.xlabel(column)
    plt.ylabel("amount_paid")
    plt.title(column + " vs electricity bill")
    plt.savefig("outputs/" + filename)
    plt.close()

def run_eda(df):
    print(df.describe())

    # Chart 1: how the bills are spread
    plt.hist(df["amount_paid"], bins=30)
    plt.xlabel("amount_paid")
    plt.ylabel("Number of households")
    plt.title("Distribution of electricity bills")
    plt.savefig("outputs/histogram.png")
    plt.close()


    # Chart 2 and 3: house area and income against the bill
    scatter_chart(df, "housearea", "housearea_vs_bill.png")
    scatter_chart(df, "ave_monthly_income", "income_vs_bill.png")
    
    
    
    # Chart 4: correlation of every column with the bill
    correlation = df.corr()["amount_paid"].drop("amount_paid")
    correlation.plot(kind="bar")
    plt.title("Correlation with electricity bill")
    plt.tight_layout()
    plt.savefig("outputs/correlation.png")
    plt.close()

    print("EDA charts saved in outputs/ folder")

   
    
   

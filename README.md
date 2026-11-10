# Electricity Bill Estimator

Predicts monthly household electricity bills using multiple linear regression based on house area, occupancy, and appliance indicators (`pandas`, `matplotlib`, `scikit-learn`).

## Team and Roles

| Member | Entry No. | Role |
| :--- | :--- | :--- |
| DIVYDAKSH-TIWARI  | 2026DAB1292 | Documentation lead |
| ASHUTOSH-KUMAR    | 2026AIB1023 | Execution lead     |
| K.N. PRAYOG       | 2026EEB1361 | PPT lead           |
| GOKUL-GARG        | 2026MCB1526 | Video lead         |


## Project Structure

```
Electricity-Bill-Estimator/
├── data/
│   └── household_energy_bill_data.csv   # dataset
├── src/
│   ├── main.py            # runs all steps
│   ├── data_cleaning.py   # loads and cleans the data
│   ├── eda.py             # data charts
│   ├── train_model.py     # trains the model and checks accuracy
│   ├── result_plots.py    # result charts
│   └── predict.py         # predicts the bill for a new house
├── outputs/               # charts, metrics.txt and the saved model
├── requirements.txt       # libraries to install
└── README.md
```

# Written by: Member 2 (Execution lead)

import pickle

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


FEATURES = ["num_rooms", "num_people", "housearea", "is_ac", "is_tv",
            "is_flat", "ave_monthly_income", "num_children", "is_urban"]
TARGET = "amount_paid"


def train_and_evaluate(df):
    X = df[FEATURES]
    y = df[TARGET]

    # 80% data for training, 20% data for testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5

    print("R2 score:", round(r2, 3))
    print("MAE     :", round(mae, 2))
    print("RMSE    :", round(rmse, 2))

    with open("outputs/metrics.txt", "w") as file:
        file.write("R2 score: " + str(round(r2, 3)) + "\n")
        file.write("MAE: " + str(round(mae, 2)) + "\n")
        file.write("RMSE: " + str(round(rmse, 2)) + "\n")
        file.write("\nCoefficients (effect of each column on the bill):\n")
        for name, value in zip(FEATURES, model.coef_):
            file.write(name + ": " + str(round(value, 4)) + "\n")
    with open("outputs/model.pkl", "wb") as file:
        pickle.dump(model, file)

    return model, y_test, y_pred, r2

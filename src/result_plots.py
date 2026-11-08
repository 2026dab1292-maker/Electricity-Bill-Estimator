import matplotlib.pyplot as plt

def make_result_plots(y_test, y_pred, r2):
    pass

    plt.scatter(y_test, y_pred, alpha=0.5)
    low = min(y_test.min(), y_pred.min())
    high = max(y_test.max(), y_pred.max())
    plt.plot([low, high], [low, high], color="red")
    plt.xlabel("Actual bill")
    plt.ylabel("Predicted bill")
    plt.title("Actual vs Predicted (R2 = " + str(round(r2, 3)) + ")")
    plt.savefig("outputs/actual_vs_predicted.png")
    plt.close()
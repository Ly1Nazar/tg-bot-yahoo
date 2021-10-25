from statsmodels.tsa.arima.model import ARIMA


def predict(data, number_of_predictions):
    model = ARIMA(data, order=(number_of_predictions, 1, 1))
    model_fit = model.fit()
    # make prediction
    arima_prediction = model_fit.predict(len(data), len(data)+number_of_predictions)
    return arima_prediction

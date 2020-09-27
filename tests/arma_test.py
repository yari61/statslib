from statslib.models.arma import ARMA

from tests.settings.autoregression import order as ar_order, parameters as ar_params
from tests.settings.moving_average import order as ma_order, parameters as ma_params

arma = ARMA(ma_order, ma_params, ar_order, ar_params)

if __name__ == "__main__":
    length = 45
    dataset = arma.generate_time_series(length=length)
    for i in range(0, length):
        forecast = arma.forecast(dataset=dataset, index=i)
        real = dataset[i]
        print(round(forecast, 2), round(real, 2), round(real - forecast, 2))

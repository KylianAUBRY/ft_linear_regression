pip install pandas
pip install matplotlib

run python3 main.py

The first program will be used to predict the price of a car for a given mileage.
Enter the mileage, it will return the estimated price based on the following assumption:

$$
estimatePrice(mileage) = {\theta 0} + ({\theta 1} * mileage)
$$

If you don't call the training program beforehand (the second program), theta0 and theta1 will be set to 0.

The second program will be used to train your model.
It will read your dataset file (data.csv) and perform a linear regression on the data.
According to the following formulas:

$$
tmp{\theta 0} = learningRate * \frac{1}{m} \sum_{i=0}^{m-1} (estimatePrice(mileage[i]) − price[i])
$$

$$
tmp{\theta 1} = learningRate * \frac{1}{m} \sum_{i=0}^{m-1} (estimatePrice(mileage[i]) − price[i])*mileage[i]
$$

To avoid overflow, I need to normalize my values in program 2 to calculate my thetas and denormalize my thetas to use them. For this, I use these formulas :

$$
km[i] = (km[i] - averageKilometer) / standardDeviationKm
$$
$$
price[i] = (price[i] - avaragePrice) / standarPrice
$$

$$
{\theta 1} = tmp{\theta 1} * \frac{standardDeviationPrice}{standardDeviationKm}
$$

$$
{\theta 0} = tmp{\theta 0} * standardDeviationPrice - {\theta 1} * averageKilometer * standardDeviationPrice
$$
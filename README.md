pip install pandas
pip install matplotlib

run python3 main.py

The first program will be used to predict the price of a car for a given mileage.
Enter the mileage, it will return the estimated price based on the following assumption:

$$estimatePrice(mileage) = {\theta 0} + ({\theta 1} * mileage)$$
$$tmp{\theta 0} = learningRate * \frac{1}{m} \sum_{i=0}^{m-1} (estimatePrice(mileage[i]) − price[i])$$

$$tmp{\theta 1} = learningRate * \frac{1}{m} \sum_{i=0}^{m-1} (estimatePrice(mileage[i]) − price[i])*mileage[i]$$

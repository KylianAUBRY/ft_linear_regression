import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

def sommeEstimatePriceTheta0(km, price, beginning, end, theta0, theta1) :
	somme = 0
	for i in range(beginning, end) :
		somme += (theta0 + (theta1 * km[i])) - price[i]
	return somme

def sommeEstimatePriceTheta1(km, price, beginning, end, theta0, theta1) :
	somme = 0
	for i in range(beginning, end) :
		somme += ((theta0 + (theta1 * km[i])) - price[i]) * km[i]
	return somme


file_path = Path('data.csv')
if (file_path.is_file()) :
	data = pd.read_csv(file_path)
else :
	print ("Error : data.csv does not exist.")
	exit () 

###################### Setting ######################

learningRate = 0.001
iteration = 2500
m = len(data)

###################### Normalize ######################

mean_km = data['km'].mean()  # Moyenne
std_km = data['km'].std()    # Écart-type
mean_price = data['price'].mean()
std_price = data['price'].std()

data['km'] = (data['km'] - mean_km) / std_km # normalisation
data['price'] = (data['price'] - mean_price) / std_price

# data['km'] /= data['km'].max()
# data['price'] /= data['price'].max()

###################### calculates ######################

theta0 = 0
theta1 = 0
tmp0 = 0
tmp1 = 0
thetaHistory = []

for i in range(0, iteration) :
	tmp0 = learningRate * (1 / m) * sommeEstimatePriceTheta0(data['km'], data['price'], 0, m, theta0, theta1)
	tmp1 = learningRate * (1 / m) * sommeEstimatePriceTheta1(data['km'], data['price'], 0, m, theta0, theta1)
	theta0 -= tmp0
	theta1 -= tmp1
	if i in [1, 10, 100, 1000] :
		thetaHistory.append([theta0, theta1])

###################### Denormalization ######################

theta1 = theta1 * (std_price / std_km)
theta0 = theta0 * std_price + mean_price - theta1 * mean_km

data['km'] = data['km'] * std_km + mean_km 
data['price'] = data['price'] * std_price + mean_price


data['price_predicted'] = theta0 + theta1 * data['km']

###################### Draw data ######################

plt.scatter(data['km'], data['price'], label='Reel value')
plt.plot(data['km'], data['price_predicted'], color='red', label=f'linear regression line {iteration}')
for i in range(0, 4) :
	thetaHistory[i][1] = thetaHistory[i][1] * (std_price / std_km)
	thetaHistory[i][0] = thetaHistory[i][0] * std_price + mean_price - thetaHistory[i][1] * mean_km

plt.plot(data['km'], thetaHistory[0][0] + thetaHistory[0][1] * data['km'], color='orange', label= "History1")
plt.plot(data['km'], thetaHistory[1][0] + thetaHistory[1][1] * data['km'], color='yellow', label= "History10")
plt.plot(data['km'], thetaHistory[2][0] + thetaHistory[2][1] * data['km'], color='green', label= "History100")
plt.plot(data['km'], thetaHistory[3][0] + thetaHistory[3][1] * data['km'], color='blue', label= "History1000")

###################### Calculates mae, mse ######################

mae = 0
mse = 0

for row in data.itertuples(index=False) :
	# le prix dans la data - le prix que je trouve avec ma formule.
	mae += abs ((row.price - (theta0 + (theta1 * row.km))))
	mse += (row.price - (theta0 + (theta1 * row.km))) **2 

mae /= len(data)
mse /= len(data)

print ("mae : ", mae, " mse : ", mse)


with open("result.txt", "w", encoding="utf-8") as f :
	f.write("theta0 : ")
	f.write(str(theta0))
	f.write( "\ntheta1 : ")
	f.write(str(theta1))

plt.legend()
plt.show()
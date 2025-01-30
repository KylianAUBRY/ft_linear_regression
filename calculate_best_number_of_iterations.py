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

def calulateMaeAndMse (data, theta1, theta0) :
	mae = 0
	mse = 0
	for row in data.itertuples(index=False) :
		# le prix dans la data - le prix que je trouve avec ma formule.
		mae += abs ((row.price - (theta0 + (theta1 * row.km))))
		mse += (row.price - (theta0 + (theta1 * row.km))) **2 
	mae /= len(data)	
	mse /= len(data)
	return mae, mse


file_path = Path('data.csv')
if (file_path.is_file()) :
	data = pd.read_csv(file_path)
else :
	print ("Error : data.csv does not exist.")
	exit() 

###################### Setting ######################

try :
	learningRate = float(input("Enter a decimal number : "))
except ValueError :
	print ("Error : You must enter a valid number!")
	exit ()

m = len(data)

###################### normalize ######################

mean_km = data['km'].mean()  # Moyenne
std_km = data['km'].std()    # Écart-type
mean_price = data['price'].mean()
std_price = data['price'].std()

denormalizeData = data.copy()
print (denormalizeData)
data['km'] = (data['km'] - mean_km) / std_km # normalisation
data['price'] = (data['price'] - mean_price) / std_price
print (denormalizeData)

# data['km'] /= data['km'].max()
# data['price'] /= data['price'].max()

###########################################################

theta0 = 0
theta1 = 0
tmp0 = 0
tmp1 = 0

tmpMse = -1
tmpMae = -1
countIteration = 0
i = 0

while (True) :
	i += 1
	tmp0 = learningRate * (1 / m) * sommeEstimatePriceTheta0(data['km'], data['price'], 0, m, theta0, theta1)
	tmp1 = learningRate * (1 / m) * sommeEstimatePriceTheta1(data['km'], data['price'], 0, m, theta0, theta1)
	theta0 -= tmp0
	theta1 -= tmp1
	mae, mse = calulateMaeAndMse(denormalizeData, theta1 * (std_price / std_km), theta0 * std_price + mean_price - (theta1 * (std_price / std_km)) * mean_km)
	if (mae < tmpMae or tmpMae == -1) :
		tmpMse = mse
		tmpMae = mae
		countIteration = 0

	countIteration += 1
	if (countIteration >= 100) :
		print ("mae : ", tmpMae, "mse : ", tmpMse, " number of iteration : ", i)
		break

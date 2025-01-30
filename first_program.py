import os

file_path = 'result.txt'

theta0 = 0
theta1 = 0

if os.path.exists(file_path) :
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			lines = file.readlines()

			for line in lines:
				if 'theta0' in line:
					theta0 = float(line.split(':')[1].strip())
				if 'theta1' in line:
					theta1 = float(line.split(':')[1].strip())
                    
	except Exception as e:
		print(f"Error reading the file : {e}")

print("theta0 : ", theta0)
print("theta1 : ", theta1)

try :
	milage = int(input("Enter a decimal number : "))
	if (milage < 0) :
		print("please enter a non-negative integer.")
		exit()
except ValueError :
	print ("Error : You must enter a valid number!")
	exit ()

estimatePrice = theta0 + (theta1 * milage)
print ("Estimate price : ", estimatePrice)
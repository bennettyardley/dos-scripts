import os, random

while True:
	randomNum = random.random()
	ranString = str(randomNum)
	os.system('mkdir ' + ranString)

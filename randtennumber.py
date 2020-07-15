
import random

numbers=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(numbers)

for i in range(0,len(numbers)):
	print(numbers[i], end =" ")

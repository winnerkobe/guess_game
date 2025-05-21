#這是一個猜數字遊戲
import random
r = random.randint(1, 100)
while True: 
	ans =int(input('請輸入一個從1到100內的整數。'))
	if ans == r:
		print('你贏了。')
		break
	elif ans < r:
		print('你輸入的數字太小了。')
	else:
		print('你輸入的數字太大了。')

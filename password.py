x = 0
while x < 3:
	password = input('請輸入密碼:')
	if password !='a123456':
		print('密碼錯誤!','還剩下',2-x,'次機會')
		x = x + 1
	elif password =='a123456':
		print('登入成功!')
		break


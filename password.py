password = 'a123456'
x = 0
while x < 3:
	pwd = input('請輸入密碼:')
	if pwd != password:
		print('密碼錯誤!','還剩下',2-x,'次機會')
		x = x + 1
	elif pwd == password:
		print('登入成功!')
		break


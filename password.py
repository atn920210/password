password = 'a123456'
x = 0
while x < 3:
	x = x + 1
	pwd = input('請輸入密碼:')
	if pwd != password:
		print('密碼錯誤!')
		if x < 3:
			print('還剩下',3-x,'次機會')
		else:
			print('沒機會嘗試了!要鎖帳號了啦!')
	elif pwd == password:
		print('登入成功!')
		break


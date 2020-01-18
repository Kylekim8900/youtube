import pyperclip
import time

f = open('result.txt', mode ='a')


while(1):
	print('Check')
	time.sleep(3)
	a = pyperclip.paste()
	f.write(a+'\n')
	if a == 'exit':
		print('END')
		break
	elif a == 'whoau':
		pyperclip.copy('you hacked')
		break

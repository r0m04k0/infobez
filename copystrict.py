import time

def granted():
	print("Программа успешно запущена.")
	time.sleep(5)

def blocked():
	print("Программа остановлена.")
	time.sleep(5)

staticParams = {
	'userName': 'romo4ko',
	'hardDriveNumber': '1920031797'
}

try:
	import getpass
	import win32api

	userName = getpass.getuser()
	hardDriveNumber = win32api.GetVolumeInformation("C:\\")

	if userName == staticParams['userName'] and str(hardDriveNumber[1]) == str(staticParams['hardDriveNumber']):
		granted()
	else:
		blocked()

except:
	blocked()





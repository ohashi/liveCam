import ui

url_base = 'http://www.qsr.mlit.go.jp/fukkoku/bousai/pc/cctv.php?cno='
url_cno =	[2059, 2060, 2061, 2062, 2063, 2037, 2039, 2047, 2048]
webviews = []
initFlag = False
	
def update(myInterface):
	global initFlag
	if initFlag == False:
		viewSelector = myInterface.superview
		for no in range(9):
			webview = viewSelector['webview'+str(no)]
			webview.load_url(url_base+str(url_cno[no]))
			webviews.append(webview)
		initFlag = True
	else:
		for no in range(9):
			webviews[no].reload()
			
v = ui.load_view()
update(v['button1'])
sc = ui.get_screen_size()
if sc[0] >= 768.0 and sc[1] >= 768.0:
	# iPad
	v.frame = (0, 0, 414, 896)
	v.present('sheet') # fullscreen
	print('iPad')
else:
	# iPhone
	v.present('sheet', orientations=['portrait'])
	print('iPhone')

ws = ui.get_window_size()
print('{0},{1}'.format(ws[0],ws[1]))



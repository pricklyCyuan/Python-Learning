#像程式設計師這樣思考
#Chapter 2 問題:側邊三角形

for raw in range(7):					
	for hashnum in range(0,4-abs(3-raw),1):	#因為Python Range 由0開始，因此優先將raw+1
		print("#", end = '')				#因為python有自動換行的功能，限制end來避免換行
	print('')								#print 一個空字串會自帶一個換行
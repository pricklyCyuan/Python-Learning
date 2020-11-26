#像程式設計師這樣思考
#Chapter 2 問題:倒直角三角形

for raw in range(5):
	for hashnum in range(0,5-raw,1):
		print("#", end = '')	#因為python有自動換行的功能，限制end來避免患行
	print('')			#print 一個空字串會自帶一個換行

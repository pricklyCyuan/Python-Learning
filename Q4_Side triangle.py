#像程式設計師這樣思考
#Chapter 2 問題:側邊三角形

for raw in range(1,8,1):					#需定義Range 改從1 開始才不會影響中間絕對值的計算
	for hashnum in range(0,4-abs(4-raw),1):	#透過4-abs(4-raw)達到遞增後遞減的效果
		print("#", end = '')				#因為python有自動換行的功能，限制end來避免換行
	print('')								#print 一個空字串會自帶一個換行
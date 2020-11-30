#像程式設計師這樣思考
#Chapter 2 問題:Luhn Checksum 第一部分 大於10的數字處理

digit = int(input('please enter a single digit number ,0-9 :'))

if (digit*2>=10):
	sum = 1 + (2*digit)%10
else:
	sum=digit
print(sum)
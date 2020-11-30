# 像程式設計師這樣思考
# Chapter 2 問題:Luhn Checksum 第一部分 簡單6位數checksum

digit = input('please enter a 6 digit number:')  # 讀取輸入值
sum = 0

for i in digit:
    i = int(i)
    sum = sum + i

if (sum % 10 == 0):
    print(digit + ' is a valid number')
else:
    print(digit + ' is a invalid number')

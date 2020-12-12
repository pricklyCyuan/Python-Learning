# 像程式設計師這樣思考
# Chapter 2 問題:Luhn Checksum 第四部分 簡單雙位數Luhn checksum
digit = input('ENTER a number with an even number of digits:')  # 讀取輸入值
sum = 0
for i in range(0, len(digit)):  								# 將Range直接帶入 input值的長度
    j = int(i) + 1  											# 定義數字從1開始
    bit = int(digit[i]) 										# 讀取 digit 字串的每個值,轉換成int型別

    if (j % 2 == 0):  											# 偶數位置
        sum = sum + bit
    else:  														# 奇數位置
        if (2 * bit >= 10):
            sum = sum + 1 + (2 * bit) % 10  					# 若double後大於10
        else:
            sum = sum + (2 * bit)  								# 若double後小於10
if (sum % 10 == 0):
    print(digit + ' is a valid number')
else:
    print(digit + ' is a invalid number')

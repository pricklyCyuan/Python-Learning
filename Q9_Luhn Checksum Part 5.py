# 像程式設計師這樣思考
# Chapter 2 問題:Luhn Checksum 第五部分 positive or negative
positive = 0
negative = 0

for i in range(1, 11):
    digit = int(input('ENTER the ' + str(i) + ' numbers:'))
    if (digit > 0):
        positive = positive + 1
    else:
        negative = negative + 1

response = input('Do you want the (p)ositive or (n)egative count? : ')

if (response == 'p'):
    print('There are ' + str(positive) + ' positive number(s)')
if (response == 'n'):
    print('There are ' + str(negative) + ' negative number(s)')

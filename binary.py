
num=input(float())

binary= ' '

while num > 0:
    if (num % 2) == 0:
        binary += '0'
    else:
        binary += '1'

    num=num // 2

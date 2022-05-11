bc = input() #base_char
hc = input() #head_char

row1 = '      ' + hc
row2 =('{0}{0}{0}{0}{0}{0}{1}{1}'.format(bc,hc))
row3 =('{0}{0}{0}{0}{0}{0}{1}{1}{1}'.format(bc,hc))

print(row1)
print(row2)
print(row3)
print(row2)
print(row1)

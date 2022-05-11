input_str=input()

input_str_no_spaces = input_str.replace(' ','')

if input_str_no_spaces==input_str_no_spaces[::-1]:
    print(input_str,'is a palindrome')

else:
    print(input_str,'is not a palindrome')

input_numbers = [int(x) for x in input().split(' ')]
input_range = [int(x) for x in input().split(' ')]

for number in input_numbers:
    if input_range[0] <= number <= input_range[1]:
        print('{}'.format(number), end = ' ')

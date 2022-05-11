user_input = input()

tokens = user_input.split()


input_data = []
for token in tokens:
    if int(token) >= 0:
        input_data.append(int(token))

input_data_sorted=sorted(input_data)

for entry in input_data_sorted:
    print('{}'.format(entry), end= ' ')
        

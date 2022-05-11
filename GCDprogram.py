num_a = int(input('Enter first positive integer: '))
print()

num_b = int(input('Enter second positive integer: '))
print()

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b
        print('num_a is {}'.format(num_a))
    else:
        num_b = num_b - num_a
        print('num_b is',num_b)
print('GCD is {}'.format(num_a))

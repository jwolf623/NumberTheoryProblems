def int2rev_binary(num):
    binary= ' '
    while num > 0:
        if (num % 2) == 0:
            binary += '0'
        else:
            binary += '1'
        num=num // 2
    return binary




if __name__ == '__main__':

    some_integer=input(int())
    rev_binary_val=int2rev_binary(some_integer)
    binary_val=rev_string(rev_binary_val)
    print(binary_val)

def is_prime(k):
    j=round(k/2)
    val=True
    for i in range(2, j+1):
        if k % i == 0:
            return False
    return True

U=()

p_nums=[]                   #Create list of ONLY prime numbers
for i in range(1,30):
    if is_prime(i)==True:
        p_nums+=[i]

tp_count = 0
for num in p_nums:
    pot_twin = num + 2
    if (is_prime(pot_twin)):
        tp_count+=1
        U+=(num,pot_twin)

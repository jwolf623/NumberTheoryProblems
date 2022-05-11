def is_prime(k):
    j=round(k/2)
    val=True
    for i in range(2, j):
        if k % i == 0:
            return False
    return True

p_nums=[]
for i in range(1,30):
    if is_prime(i)==True:
        p_nums+=[i]

tp_count=0
for num in p_nums:
    pot_twin = num + 2
    if (is_prime(pot_twin)):
        tp_count+=1
        print(num, pot_twin,"are twin primes.")

print('The number of twin primes is:', tp_count)



#Sort through the list so that only the
#numbers that sequentially differ by two
#are stored

#Now, create a process to go through p_nums
#and sequentially check for primes numbers that
#that have a difference of two
#find a list of EVERY OTHER  prime number

#create an index to find every other prime
#If the difference between the first prime number
#and second prime number is two make the twin primes
#into a tuple and print it as a tuple

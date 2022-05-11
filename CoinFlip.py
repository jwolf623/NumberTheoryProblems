import random as rand
results = []

def coin_flip(n):
    n=int(input('Enter how many coin flips are desired.'))
    res = ''
    for i in range(0,n):

        val=rand.randint(0,1)


        if val == 1:
            res = 'H'
        elif val == 0:
            res = 'T'


        results.append(val)
        print(res,end='')






num_heads = results.count(1)
num_tails = results.count(0)

print('For',n,'coin flips, tails appeared',num_tails,'times while heads appeared',num_heads,'times.')

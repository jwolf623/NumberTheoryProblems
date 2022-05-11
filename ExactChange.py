tot_change = int(input())

if tot_change == 0:
    print("No change")

ndol = tot_change // 100

tot_change -= ndol*100
nq = tot_change // 25

tot_change -= nq*25
nd = tot_change // 10


tot_change -= nd*10
nn = tot_change // 5

tot_change -= nn*5
np = tot_change // 1

if ndol > 1:
    print('{} dollars'.format(ndol))
elif ndol == 1:
    print('{} dollar'.format(ndol))
else:
    pass

if nq > 1:
    print('{} quarters'.format(nq))
elif nq == 1:
    print('{} quarter'.format(nq))
else:
    pass

if nd > 1:
    print('{} dimes'.format(nd))
elif nd == 1:
    print('{} dime'.format(nd))
else:
    pass

if nn > 1:
    print('{} nickels'.format(nn))
elif nn == 1:
    print('{} nickel'.format(nn))
else:
    pass

if np > 1:
    print('{} pennies'.format(np))
elif np == 1:
    print('{} penny'.format(np))
else:
    pass

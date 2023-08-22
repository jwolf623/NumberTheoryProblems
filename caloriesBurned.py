age=int(input())
wt=int(input())
hr=int(input())
time=int(input())

calBurned_women = ((age*0.074) - (wt * 0.05741) + (hr * 0.4472) - 20.4022)*time / 4.184
calBurned_men = ((age*0.2017) + (wt * 0.09036) + (hr * 0.6309) - 55.0969) * time / 4.184


print('Women: {:.2f} calories'.format(calBurned_women))
print('Men: {:.2f} calories'.format(calBurned_men))

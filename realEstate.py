curr_pr=int(input())
lastmonth_pr=int(input())

difference=curr_pr - lastmonth_pr

summary_pr = (curr_pr*0.051)/12

print('This house is ${}. The change is ${} since last month.'.format(curr_pr, difference))
print('The estimated monthly mortgage is ${:.2f}.'.format(summary_pr))

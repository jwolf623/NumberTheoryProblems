def driving_cost(miles_driven,mpg,dpg):
    cost=(1/mpg) * dpg * miles_driven
    return cost


if __name__ == '__main__':
    # Type your code here.
    mpg=float(input())
    dpg=float(input())


    cost_10 = driving_cost(10,mpg,dpg)
    cost_50 = driving_cost(50,mpg,dpg)
    cost_400 = driving_cost(400,mpg,dpg)

    print('{:.2f}'.format(cost_10))
    print('{:.2f}'.format(cost_50))
    print('{:.2f}'.format(cost_400))

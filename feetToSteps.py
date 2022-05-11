def feet_to_steps(feet):
    steps=feet/2.5
    return steps


if __name__ == '__main__':
    # Type your code here.

    feet_walked=input(float())
    steps_w=feet_to_steps(feet_walked)

    print(steps_w)

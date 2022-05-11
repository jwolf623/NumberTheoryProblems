
def is_prime(k):
    j=round(k/2)
    val=True
    for i in range(2, j):
        if k % i == 0:
            return False
    return True

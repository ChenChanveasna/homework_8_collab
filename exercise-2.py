def index_power(numbers, n):
    if len(numbers)-1 >= n:
        res = numbers[n]**n
        return res
    else:
        return -1

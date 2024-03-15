def replace_last(numbers):
    empty = []
    if len(numbers) <= 1:
        return numbers
    else:
        empty.append(numbers[-1])
        for i in range (0, len(numbers)-1):
            empty.append(numbers[i])
        return empty    
    
print(replace_last([2, 3, 4, 1]))
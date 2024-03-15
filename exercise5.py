def reverse_ascending(numbers):
    empty = []
    temp = []
    if not numbers:
        return empty
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            temp.append(numbers[i])
        else:
            temp.append(numbers[i])
            for num in temp[::-1]:
                empty.append(num)
            temp = []
    #Adding the last subsequence since the above loop will stuck at index len(numbers) - 2
    temp.append(numbers[-1])
    for num in temp[::-1]:
        empty.append(num)
    return empty

print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))
print(reverse_ascending([1, 3, 2, 4, 6, 5]))
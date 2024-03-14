def replace_last(numbers):
    
    if not numbers:
        return []
    
    num = len(numbers)
    result = numbers[num - 1]

    numbers.pop()
    numbers.append(result)
    
    return numbers
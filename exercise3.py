def remove_all_after(numbers, n):
    new_list = []
    for x in numbers:
        if x != n:
            new_list.append(x)
        elif x == n:
            new_list.append(x)
            break
    return new_list

def remove_smallest(numbers):
    if numbers:
        min_index = numbers.index(min(numbers))
        return list(j for i, j in enumerate(numbers)
                    if i != min_index)
    return numbers

test = [1, 2, 3, 4, 5]
print(remove_smallest(test))

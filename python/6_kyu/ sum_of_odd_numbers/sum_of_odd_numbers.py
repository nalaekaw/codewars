def row_sum_odd_numbers(n):
    start = n * (n - 1) + 1
    end = n * (n + 1) + 1

    return sum(i for i in range(start, end, 2))

# def row_sum_odd_numbers(n):
#     return n ** 3


print(row_sum_odd_numbers(41))

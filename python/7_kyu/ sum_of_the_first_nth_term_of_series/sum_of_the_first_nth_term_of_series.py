# def series_sum(n):
#
#     if not n:
#         return "0.00"
#     elif n == 1:
#         return "1.00"
#
#     series = sum((1/i for i in range(4, (n*3)+1, 3))) + 1.0
#
#     return "{:0.2f}".format(series)

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))


print(series_sum(5))

print(round(sum([1, 1/4, 1/7, 1/10, 1/13]), 2))

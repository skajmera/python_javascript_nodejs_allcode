def pattern(number):
    if number == 1:
        return 1
    else:
        return pattern(number-1) + 3 
pri=(pattern(6))
print(pri)


# def pattern(number):
#     if number == 1:
#         return 10
#     elif number % 2 == 0:
#         return pattern(number - 1) + 1
#     else:
#         return pattern(number - 1) * 10 
# print(pattern(10))

# def sum_list(lis):
#     if len(lis)==1:
#         return lis[0]
#     return lis[0] + sum_list(lis[1:])

# print (sum_list([1, 4, 7, 10]))












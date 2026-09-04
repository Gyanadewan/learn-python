def even_sum_numbers():
    sum = 0
    for num in range(1,101):
        if num %2 == 0:
            sum = sum+num
    return sum

print(even_sum_numbers())
def count_d(num):
    count = 0
    while num > 0:
     count += 1
     num = num // 10
     
    return count


print(count_d(123456))
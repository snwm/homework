def average(lst):
    summ_numbers = 0
    for i in lst:
        summ_numbers += i
    
    middle_numb = summ_numbers / len(lst)
    return round(middle_numb, 3)

print(average([14, 8, 3, 1, 89, 2, 45]))
print(average([0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45]))
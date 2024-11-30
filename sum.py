def sum_of_numbers(num):
    sum = 0
    for i in num:
        sum+=i
    return sum
lst = eval(input("Enter the list of numbers: "))
print(sum_of_numbers(lst))

# ЛР1 Задание 1:
#Сумма простых делитей числа
'''def is_prime(numb):
    if numb < 2:
        return False
    for i in range(2, int(numb ** 0.5) + 1):
        if numb % i == 0:
            return False
    return True

def sum_divisors(numb):
    divisors = []
    
    for i in range(1, numb + 1):
        if numb % i == 0:
            divisors.append(i)

    prime_divisors_sum = sum(i for i in divisors if is_prime(i))
    
    return prime_divisors_sum

number = int(input("Введите число: "))
print("Сумма простых делителей числа:", sum_divisors(number))

'''
# Задание 2

'''
numper = int(input("Введиет число: "))
numb_string = str(numper)
count=1
for i in range (1,len(numb_string)+1):
    if(i%2!=0 and i>3):
        count+=1
print(count)
'''

# Задане 3 
# Найти произведение таких делителей числа, сумма цифр которых меньше, чем сумма цифр исходного числа.

'''
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
def find_divisors_product(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    orig_sum_digits = sum_digits(n)

    product = 1
    for divisor in divisors:
        if sum_digits(divisor) < orig_sum_digits:
            product *= divisor

    return product


print("Введите число :")
number = int(input())
result = find_divisors_product(number)
print(f"Произведение делителей числа {number}, сумма цифр которых меньше суммы цифр исходного числа: {result}")
'''
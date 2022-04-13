# Дано ціле число N (> 0). Знайти число, отримане при прочитанні числа N справа наліво та добуток
# його цифр.
n = int(input("enter the number = "))
if n <= 0:
    exit(0)
    print("Число повинно бути більшим за 0")


def reverse_product(n):
    reverse = 0
    product = 1
    while n > 0:
        last = n % 10
        reverse = reverse * 10 + last
        n = n // 10
        product *= last
    print(reverse)
    print(product)


reverse_product(n)



# Дано ціле число N (> 1). Послідовність чисел Фібоначчі FK визначається наступним чином:F1 = 1,
# F2 = 1, FK = FK-2 + FK-1, K = 3, 4, .... Перевірити, чи є число N числом Фібоначчі. Якщо є, то вивести
# true, якщо ні - вивести false
n = int(input("enter the number = "))
if n <= 1:
    exit(0)
    print("Число повинно бути більшим за 1")


def fibonachi(n):
    fib = [0]*100
    fib[0] = 1
    fib[1] = 1
    for i in range(2, 99, 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] == n:
            print('true')
            exit(0)
        if fib[i] > n:
            print(bool(0))
            exit(0)


fibonachi(n)

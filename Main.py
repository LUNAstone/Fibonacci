def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        tmp = a
        a = b
        b += tmp
        print(a)

if __name__ == '__main__':
    loops = int(input("How many loops would you like? "))
    fibonacci(loops)
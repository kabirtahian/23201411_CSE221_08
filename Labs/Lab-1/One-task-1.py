def OddEven(t):
    for i in range(t):
        n = int(input())
        if n % 2 == 0:
            print(f"{n} is an Even number.")
        else:
            print(f"{n} is an Odd number.")

OddEven(int(input()))

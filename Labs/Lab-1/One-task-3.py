n = input()
a, b = n.split(" ")

num = input()
val = num.split(" ")

for i in range(int(b)):
    print(val[int(b)-1 - i], end=" ")   
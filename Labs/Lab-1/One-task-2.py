def calculator(t):
    for i in range(t):
        n = input()
        val = n.split(' ')
        
        if val[2] == "+":
            result = float(int(val[1]) + int(val[3]))
            print(result)
        elif val[2] == "-":
            result = float(int(val[1]) - int(val[3]))
            print(result)
        elif val[2] == "*":
            result = float(int(val[1]) * int(val[3]))
            print(result)
        elif val[2] == "/":
            result = float(int(val[1]) / int(val[3]))
            print(result)

    

calculator(int(input()))
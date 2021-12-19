def read_file(input):
    a = []
    with open(input, 'r') as f:
        for line in f.readlines():
            a += list(map(int, line.split()))
    return a


def summa(input):
    arr = read_file(input)
    sum = 0
    for i in arr:
        sum += i
    print("Sum:", sum)
    print()
    return sum


def multiplication(input):
    arr = read_file(input)
    mult = 1
    for i in arr:
        mult *= i
    print("Mult:", mult)
    print()
    return mult

def maximum(input):
    arr = read_file(input)
    max = -10000000000000000
    for i in arr:
       if i > max:
           max = i
    print("Max: ", max)
    print()
    return max

def minimum(input):
    arr = read_file(input)
    min = 10000000000000000
    for i in arr:
        if i < min:
            min = i
    print("Min: ", min)
    print()
    return min


def count(input):
    arr = read_file(input)
    cnt = 0
    for elem in arr:
        cnt += 1
    print("Count of elements in array: ", cnt)
    print()
    return cnt


def write_file(input, arr):
    with open(input, 'w') as f:
        for i in arr:
            f.write(str(i) + " ")

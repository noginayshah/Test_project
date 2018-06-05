li = [-20, -5, 10, 15]

n = len(li)
def list():
    for j in range(0, n-1):
        for i in range(0, n - j - 1):
            if abs(li[i]) < abs(li[i + 1]):
                li[i], li[i + 1] = li[i + 1], li[i]
        print(j + 1, "Проход цикла - " , end=" ")
        print(li)
    print(li)
list()
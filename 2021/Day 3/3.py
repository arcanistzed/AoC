array = open("2021/Day 3/data.txt", "r", encoding="UTF-8").read().splitlines()

gamma = []
epsilon = []

for i in range(12):
    col = list(map(lambda e: e[i], array))

    zero = len(list(filter(lambda x: x == "0", col)))
    one = len(list(filter(lambda x: x == "1", col)))

    gamma.append("0" if zero > one else "1")
    epsilon.append("0" if zero < one else "1")
print(int("".join(gamma), 2) * int("".join(epsilon), 2))

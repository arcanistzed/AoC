import itertools

array = open("2021/Day 3/data.txt", "r", encoding="UTF-8").read().splitlines()

oxygen = []
co2 = []


for bit in array:
    for i in range(5):
        # get a column of bits
        col = list(map(lambda e: e[i], array))
        print(col)

        # count zeros and ones
        zero = len(list(filter(lambda x: x == "0", col)))
        one = len(list(filter(lambda x: x == "1", col)))

        # go through the array of bits
        for x in array:
            # if there are more zeros than ones, remove anything that does not have a zero at this index
            if zero > one:
                if x[i] != "0":
                    array.pop(bit)
            # if there are more ones than zeros, remove anything that does have a zero at this index
            else:
                if x[i] == "0":
                    array.pop(bit)
print(array)

# print(int("".join(oxygen), 2) * int("".join(co2), 2))

# for i in range(17):
#     print("{0:>2} in binary is {0:>08b}".format(i))
#
# for i in range(17):
#     print("{0:>2} in octal is {0:>02o}".format(i))
#
# x = 0x20
# y = 0x0a
#
# print(x)
# print(y)
# print(x-y)
#
# print(0b01100)


def binary(num, n):
    a = []
    while True:
        if (num/n) > 1:
            a.append(num % n)
            num = num//n
        elif (num/n) == 1:
            a.append(num % n)
            num = num//n
        else:
            a.append(num % n)
            break
    b = ""
    for i in a[::-1]:
        b += str(i)
    return b


# for i in reversed(binary(16, 2)):
#     print(i)
print(binary(0, 2))

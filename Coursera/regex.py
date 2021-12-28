#
# pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
# new_pattern = r"\1\2\3"
#
# user_input = input()
# new_user_input = re.sub(pattern, new_pattern, user_input)
#
# print(new_user_input)


# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X.*', line):
#         print(line)


# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X-\S+: \d', line):
#         print(line)

# x = 'From: Using the : character'
# y = re.findall('^F.+?:',x)
# print(y)

# hand = open('mbox-short.txt')
# line = hand.read()
# y = re.findall("<(\S+@\S+)>",line)
# for k in y:
#     print(k)
#
# hand = open('mbox-short.txt')
# numlist = []
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)',line)
#     if len(stuff) !=1: continue
#     num = float(stuff[0])
#     numlist.append(num)
# print('Maximum:', max(numlist))


import re

print(sum([int(k) for k in re.findall('[0-9]+',open('regex_test.txt').read())]))

x = 12
if x < 5:
print("smaller")
else:
    print("bigger")
print("all done")
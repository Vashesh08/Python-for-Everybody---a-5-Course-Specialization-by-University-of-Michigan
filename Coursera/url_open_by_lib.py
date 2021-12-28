import re, urllib.request, urllib.error

fhand = urllib.request.urlopen('https://www.google.com/')

count = {}
g = []
for line in fhand:
    words = line.decode().strip()
    if re.search('href.*', words):
        print(words)
    # print(words)
    # words = words.split()
    # for word in words:
    #     count[word] = count.get(word, 0) + 1

# print(count)

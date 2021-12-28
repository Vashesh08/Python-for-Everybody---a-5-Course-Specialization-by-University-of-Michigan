with open('Jabberwocky.txt', 'r', encoding='windows-1252') as jabber:
    for line in jabber:
        print(line.rstrip())



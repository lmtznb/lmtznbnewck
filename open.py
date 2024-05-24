print(1, 2, 3)
fp = open('../../Downloads/untitled/untitled/test.txt', "w")
print(1, 2, 3, sep='---', end='<+++>', file=fp)
fp.close()
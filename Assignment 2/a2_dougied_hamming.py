import sys

hashVal = sys.argv[1]
hashVal2 = sys.argv[2]

diffs = 0
for ch1, ch2 in zip(hashVal, hashVal2):
    if ch1 != ch2:
        diffs += 1

print (diffs)

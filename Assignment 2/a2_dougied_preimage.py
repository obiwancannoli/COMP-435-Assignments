import hashlib
import time
import itertools

with open("hashstring", 'r') as input_file:

    for line in input_file:
        msg = hashlib.sha256(line)

    print(msg.hexdigest())

    alphabet = "abcdedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_."

    start = time.time()
    counter = 1
    charLength = 1

    for charLength in range(24):
        passwords = (itertools.product(alphabet, repeat=charLength))
        for i in passwords:
            counter += 1
            i = str(i)
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")

        hashedVal = hashlib.sha256(i)
        print(i)

        if hashedVal.hexdigest() == msg.hexdigest()[:24]:
            end = time.time()
            timeTaken = end-start
            print(timeTaken)
            exit()


for k in range(3, 21):
    s = ""
    for i in range(1, k):
        for n in range(i + 1, k):
            if k % (i + n) == 0:
                s = s + str(i) + str(n)
    print(k, s)


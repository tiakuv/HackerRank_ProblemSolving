def plusMinus(arr):
    pos = 0
    neg = 0
    nul = 0

    for a in arr:
        if a > 0:
            pos += 1
        elif a < 0:
            neg += 1
        else:
            nul += 1

    print ("%.6f\n%.6f\n%.6f" % (pos/len(arr), neg/len(arr), nul/len(arr)))
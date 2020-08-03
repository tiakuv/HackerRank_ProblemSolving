def countApplesAndOranges(s, t, a, b, apples, oranges):
    res_a = 0
    res_ora = 0
    for apple in apples:
        if apple + a >= s and apple + a <= t:
            res_a += 1
    for orange in oranges:
        if orange + b >= s and orange + b <= t:
            res_ora += 1
    print(res_a)
    print(res_ora)
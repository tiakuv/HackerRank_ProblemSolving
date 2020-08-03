def kangaroo(x1, v1, x2, v2):
    if (v1-v2) > 0:
        res = (x2-x1)/(v1-v2)
        if res.is_integer() and res >= 0:
            return "YES"
    return "NO"
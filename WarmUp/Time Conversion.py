def timeConversion(s):
    hour_str = s[:2]
    hour = int(hour_str)
    part = s[-2:]
    if part == "PM" and hour >= 1 and hour <= 11:
        s = s.replace(hour_str, str(hour+12))
    elif part == "AM" and hour_str == "12":
        s = s.replace(hour_str, "00")
    return s[:8]
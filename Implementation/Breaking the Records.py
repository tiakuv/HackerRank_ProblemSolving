def breakingRecords(scores):
    max_ = [scores[0]]
    min_ = [scores[0]]
    flag_max = 0
    flag_min = 0
    for i in range(1, len(scores)):
        if scores[i] > max_[i-1]:
            max_.append(scores[i])
            flag_max += 1
        else:
            max_.append(max_[i-1])
        if scores[i] < min_[i-1]:
            min_.append(scores[i])
            flag_min += 1
        else:
            min_.append(min_[i-1])
    return (flag_max, flag_min)
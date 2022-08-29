
with open('expectedpredicted.txt', 'r') as fp:
    fp.readline()
    tp, fpo = 0, 0
    for line in fp:
        spl = line.split(',')
        print(spl)
        if spl[0].strip() == spl[1].strip():
            tp += 1
            print("Same value")
        else:
            fpo += 1
            print('Not same')
    print("True Positive=", tp, "False Positive: ", fpo)

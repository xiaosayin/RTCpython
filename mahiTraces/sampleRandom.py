import random

def getT(minT, maxT):
    return random.randint(minT, maxT)

def getR(minRate, maxRate, delta):
    #delta = 1000
    cnt = 0
    rate = random.gauss((minRate + maxRate) / 2, delta)
    while rate < minRate or rate > maxRate:
        if cnt < 1000:
            rate = random.gauss((minRate + maxRate) / 2, delta)
        else:
            if rate > maxRate:
                rate = maxRate
            if rate < minRate:
                rate = minRate
        cnt += 1
    return int(rate)

def getL(minLoss, maxLoss):
    cnt = 0
    delta = 60
    loss = random.gauss(minLoss, delta)
    while loss > maxLoss or loss < minLoss:
        if cnt < 1000:
            loss = random.gauss(minLoss, delta)
        else:
            if loss > maxLoss:
                loss = maxLoss
            if loss < minLoss:
                loss = minLoss
        cnt += 1
    return float(int(loss)/ 1000)

def getD(minDelay, maxDelay):
    return random.randint(minDelay, maxDelay)

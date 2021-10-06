import pandas as pd
import math

def laplaceNoise(x,GS,u,epsilon):
    b = GS/epsilon
    if x<u:
        x = u-x
    else:
        x = x-u
    return math.exp(-x/b)/(2*b)

def resultWithNoise():
    data = pd.read_csv('adult.data', sep=', ', header=None, engine='python')
    cols = data.loc[data[0]>25,0]
    GS = max(cols)/ len(cols.index)
    u = sum(cols)/ len(cols.index)
    print('GS = {}'.format(GS))
    epsilon = [0.5, 1]
    b = [(e, GS/e) for e in epsilon]
    variance = [(x[0], 2*(x[1]**2)) for x in b]
    print("variance for different epsilon: {}".format(variance))
    average_age = sum(cols)/len(cols.index)
    resultWithNoise = [(epsilon, average_age + laplaceNoise(average_age, GS, u, epsilon)) for epsilon in epsilon]
    print("result of querying avarage age that is over 25 with noise for differet epsilon: {}".format(resultWithNoise))

if __name__ == '__main__':
    resultWithNoise()
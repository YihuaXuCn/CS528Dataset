import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def userDE(row, epsilon, d, p, q, Domain):
  x = row[0]
  head = 1
  tail = -1
  toss = np.random.choice([head, tail],p = [0.5, 0.5])
  rndP = [q]*d
  rndP[Domain.index(x)] = p

  if toss == 1:
    y = x
  else:
    y = np.random.choice(Domain, p = rndP)
  return y

def userUE(epsilon, bitString):
  q = 1/((np.e)**(epsilon/2)+1)
  p = 1-q
  flip = -1
  remain = 1
  return [ int(not bool(bit)) if np.random.choice([flip, remain], p = [q, p]) == flip else bit for bit in bitString]

def convert2vector(row, d, minAge):
  initial = [0]*d
  initial[row[0] - minAge] = 1
  return initial

def DE_UE(epsilon, Domain, ages):
  # for DE protocol:
  d = len(Domain)
  p = (np.e)**epsilon/((np.e)**epsilon+d-1)
  q = 1/((np.e)**epsilon+d-1)
  # client
  ages[len(ages.columns)] = 0
  ages[len(ages.columns)-1] = ages.apply(userDE, 1, False, 'reduce', (epsilon, d, p, q, Domain))
  statisticTru = {key:len(ages.loc[ages[0] == key,:].index) for key in Domain}

  # server:
  n = len(ages.index)
  serverDE = lambda p, q, Iv, n: (Iv - n*q)/(p - q)
  statistic = {key:serverDE(p, q, value, n) for (key, value) in statisticTru.items()}

  # for UE protocol:
  # ages = data.loc[:,[0]]
  n = len(ages.index)
  q = 1/((np.e)**(epsilon/2)+1)
  p = 1-q
  # client
  flip = 1
  remain = -1
  # convert age to vector for each row
  d = max(ages[0].to_numpy().tolist()) - min(ages[0].to_numpy().tolist()) + 1
  ages[len(ages.columns)] = 0
  ages[len(ages.columns)-1] = ages.apply(convert2vector, 1, False, 'reduce', (d, Domain[0]))
  ages
  userUE = lambda row : np.asarray( [ int(not bool(bit)) \
                                if np.random.choice([flip, remain], p = [q, p]) == flip else bit for bit in row[len(ages.columns)-2]] )
  ages[len(ages.columns)] = 0
  ages[len(ages.columns)-1] = ages.apply(userUE, 1, False, args=())
  ages[len(ages.columns)-1].shape,
  # import matplotlib.pyplot as plt
  # l1= sum([np.abs()])

  tmp = np.matrix([x.tolist() for x in ages[len(ages.columns)-1].to_numpy().tolist()]).T
  tmp = tmp.sum(axis = 1)
  tmp = tmp.T
  sigmaY = tmp.tolist()[0]
  f = lambda lv, n, p, q : (lv-n*q)/(p-q)
  estimation = [f(lv, n, p, q) for lv in sigmaY]
  estimation
  tmp = np.matrix([x for x in ages[len(ages.columns)-2].to_numpy().tolist()]).T
  tmp = tmp.sum(axis = 1)
  tmp = tmp.T
  truY = tmp.tolist()[0]

  l1Dist = lambda x,y: np.abs(x-y)
  UEs = sum([l1Dist(noise, tru) for (tru, noise) in zip(truY,estimation)])
  DEs = sum([l1Dist(noise, tru) for (tru, noise) in zip(statisticTru,statistic)])
  return UEs, DEs

def taskb():
  epsilons = list(range(1,11))
  Domain = sorted(list(set(ages.to_numpy().reshape((ages.shape[0])).tolist())))
  uel1 = []
  del1 = []
  for epsilon in epsilons:
    a, b = DE_UE(epsilon, Domain, ages)
    uel1.append(a)
    del1.append(b)
  axisX = epsilons
  print(axisX, uel1, del1)
  plt.plot(axisX, uel1, 'b*', del1, 'ro')
  plt.axis([0, 11, 0, 30000])
  plt.show()


def taskc():
  data = pd.read_csv('adult.data', sep=', ', header=None, engine='python')
  ages = data.loc[:,[0]]
  epsilon = 2
  uel1 = []
  del1 = []
  agesStep = round(len(ages.index)*0.1)
  agesSet = [ages.head(i*agesStep) for i in list(range(1, 11))]
  DomainSet = [sorted(list(set(ages.to_numpy().reshape((ages.shape[0])).tolist()))) for ages in agesSet]
  axisX= [len(ages.index) for ages in agesSet]
  for ages, Domain in zip(agesSet, DomainSet):
    a, b = DE_UE(epsilon, Domain, ages)
    uel1.append(a)
    del1.append(b)
  axisX = [len(ages.index) for ages in agesSet]
  print(axisX)
  print( uel1)
  print( del1)
  plt.plot(axisX, uel1, 'b*', del1, 'ro')
  plt.axis([min(axisX), max(axisX), 0, 20000])
  plt.show()


if __name__ == '__main__':
  taskb()
  taskc()
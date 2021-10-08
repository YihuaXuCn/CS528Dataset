import numpy as np
import pandas as pd
import numpy as np

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

data = pd.read_csv('adult.data', sep=', ', header=None, engine='python')
ages = data.loc[:,[0]]
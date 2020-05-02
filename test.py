import random as rand
from Bio.Seq import Seq
from phe import paillier


def walk(target,rang,start):
    pos = start
    step = 0
    while pos != target:
        #print(pos)
        if pos == target:
            return step
        if pos == 0:
            step += 1
            pos += 1
            continue
        if pos == rang:
            step += 1
            pos -= 1
            continue
        x = rand.randint(1,2)
        if x == 1:
            step += 1
            pos +=1
            continue
        else:
            step += 1
            pos -= 1
    return step

z = 0
n = 10000
start = 7
maximum = 12
stop = 7
until = maximum
'''
for j in range(0,until+1):
    for i in range(0,n):
        z +=walk(j,maximum,start)
    print(str(start) +" "+ str(j) + " " + str(z/n))
    z = 0
'''

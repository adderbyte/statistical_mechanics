import random, pylab

import random

def markov_disks_boxV(N, sigma,L):
    
    condition = False
    sigma = 0.15
    sigma_sq = sigma ** 2
    delta = 0.01
    #n_steps = 1000
    #
    #print(L)
    initial_config = L # store initial configuration
    count=0
    while condition == False:
        for k in range(1, N):
                a=random.choice(L)
                #print(k)
                rand =(a[0] + random.uniform(-delta, delta), 
                     a[1] + random.uniform(-delta, delta)) 
                #print('pass',k,rand)
                min_dist = min((rand[0] - c[0]) ** 2 + (rand[1] - c[1]) ** 2 for c in L if c != a)
                box_cond = min(rand[0], rand[1]) < sigma or max(rand[0], rand[1]) > 1.0 - sigma
                #print(min_dist, box_cond)
                if  not (box_cond or min_dist < 4.0 * sigma ** 2):
                    condition = True
                    a[:] = rand

                else:
                    condition = True
                    L=initial_config # if configuration is no valid then return the initial config stored in t
                    break
    L= [tuple(i) for i in L]  
    return L

N = 4
sigma = 0.1197
n_runs = 20000000
L = [[0.27, 0.20], [0.28, 0.79], [0.73, 0.27], [0.73, 0.73]]
histo_data = []
pos=L
for run in range(n_runs):
    if run> 0:
        pos = [list(i) for i in pos]
    pos = markov_disks_boxV(N, sigma,pos)
    #print(pos)
    
    for k in range(len(pos)):
        #print(pos)
        histo_data.append(pos[k][0])
pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('x')
pylab.ylabel('frequency')
pylab.title('Markov  sampling: x coordinate histogram (density eta=0.18)')
pylab.grid()
pylab.savefig('markov_disks_histo.png')
pylab.show()
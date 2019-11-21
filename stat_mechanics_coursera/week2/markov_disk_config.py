import random

def markov_disks_boxV(N, sigma,L):
    
    condition = False
    sigma = 0.15
    sigma_sq = sigma ** 2
    delta = 0.01
    #n_steps = 1000
    #L = [[0.27, 0.20], [0.28, 0.79], [0.73, 0.27], [0.73, 0.73]]
    #print(L)
    t = L
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
                    L=t
                    break
    L= [tuple(i) for i in L]  
    return L



L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]

n_steps = 10000
sigma = 0.15
del_xy = 0.05

conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
hits = {conf_a: 0, conf_b: 0, conf_c: 0}
configurations = [conf_a, conf_b, conf_c]

for conf in configurations: 
    x_vec = L
    for steps in range(n_steps):
        #rint(steps)
       #print(x_vec)
        condition_hit = True
        if steps > 0 :
            x_vec= [list(i) for i in x_vec]
        x_vec = markov_disks_boxV(4, sigma, x_vec)
        #for i in configurations:
        for b in conf:
            #for b in conf:
            condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in x_vec) < del_xy
            condition_hit *= condition_b
            #hits[conf] += 1
        if condition_hit:
            hits[conf] += 1
    
    print ('config: ',conf,', number of hits: ' ,hits[conf])

  
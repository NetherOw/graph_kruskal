import random

def main(edgeprob, nodeamt):
    
    edgeprob = 1-edgeprob
    edgeweightmax=10
    node_from = []
    node_to = []
    node_weight = []
    i=1
    j=0
    h=0 

    while i < nodeamt:
        node_from.append(i)
        node_to.append(j)
        j+=1
        if i == node_from.count(i):
            i+=1
            j=0
        node_weight.append(random.randint(1, edgeweightmax))

    i=0
    j=0
    h=len(node_from)
    node_f_res = []
    node_t_res = []
    node_w_res = []



    while i<h:
        j=random.random()
        if j > edgeprob:
            node_f_res.append(node_from[i])
            node_t_res.append(node_to[i])
            node_w_res.append(node_weight[i]) 
        i+=1

    i=0
    j=0
    h=len(node_f_res)
    node_from = []
    node_to = []
    node_weight = []

    while i<h:
        node_from.append(node_f_res[i])
        node_to.append(node_t_res[i])
        node_from.append(node_t_res[i])
        node_to.append(node_f_res[i])
        node_weight.append(node_w_res[i])
        node_weight.append(node_w_res[i])
        i+=1


    i=0
    j=0
    h=len(node_from)
    node_f_res = []
    node_t_res = []
    node_w_res = []


    zipped = zip(node_from, node_to, node_weight)
    sortedl = sorted(zipped)
    a, b, c = zip(*sortedl)
    node_from = list(a)
    node_to = list(b)
    node_weight = list(c)

    return node_from, node_to, node_weight


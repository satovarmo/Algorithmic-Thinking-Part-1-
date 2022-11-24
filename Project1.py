EX_GRAPH0={0:{1,2},1:set(),2:set()}
EX_GRAPH1={0:{1,4,5},1:{2,6},2:{3},3:{0},4:{1},5:{2},6:set()}
EX_GRAPH2={0:{1,4,5},1:{2,6},2:{3,7},3:{7},4:{1},5:{2},6:set(),7:{3},8:{1,2},9:{0,3,4,5,6,7}}

def make_complete_graph(num_nodes):
    graf=dict()
    for num in range (0,num_nodes):
        setady=set()
        for num1 in range(num):
            setady.add(num1)
        for num1 in range(num+1,num_nodes):
            setady.add(num1)
        graf[num]=setady
    return graf

def compute_in_degrees(digraph):
    in_degrees=dict()
    for node in digraph:
        in_degrees[node]=0
    for node in digraph:
        for nodeady in digraph[node]:
            in_degrees[nodeady]+=1
    return in_degrees    

def in_degree_distribution(digraph):
    ind=compute_in_degrees(digraph)
    distr=dict()
    for node in ind:
        distr[ind[node]]=0
    for node in ind:
        distr[ind[node]]+=1
    return distr
import random
import CodeSkulptor
import Project1
import alg_dpa_trial
import matplotlib.pyplot as plt

grafo=CodeSkulptor.load_graph('citationData.txt')
inDegDistr=Project1.in_degree_distribution(grafo)
def norma(dicci):
    sum=0
    for k in dicci.values():
        sum=sum+k
    for k in dicci.keys():
        dicci[k]=dicci[k]/sum
    return dicci    


def plot(graph, name, subplot=None, filename=None):
    if subplot:
        plt.subplot(subplot)
    plt.plot(graph.keys(), graph.values(), 'bo', ms=2.0)
    plt.loglog()
    plt.title('Normalized in-degree distribution of a %s graph (log-log)' % name)
    plt.xlabel('In-degree')
    plt.ylabel('Normalized weight')
    plt.xlim(0, 1000)
    plt.tight_layout()
    if filename:
        plt.savefig(filename)


def question1(subplot=None, filename=None):
    normed = norma(inDegDistr)
    plot(normed, 'citation', subplot, filename)


def algorithm_er(n, p):
    graph = {key: set() for key in range(n)}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if random.random() < p:
                graph[i].add(j)
            if random.random() < p:
                graph[j].add(i)

    return graph


def question2(subplot=None, filename=None):
    rnd = algorithm_er(3000, 0.1)
    normed = norma(Project1.in_degree_distribution(rnd))
    plot(normed, 'random generated', subplot, filename)

def avg_out_degree(graph):
    N = float(len(graph))
    return sum(len(x) for x in graph.values()) / N

    
def algorithm_dpa(n, m):
    graph = Project1.make_complete_graph(m)
    dpa = alg_dpa_trial.DPATrial(m)
    for i in range(m, n):
        graph[i] = dpa.run_trial(m)
    return graph


def question3(subplot=None, filename=None):
    print('avg_out_degree', avg_out_degree(grafo))
    dpa = algorithm_dpa(27700, 13)
    normed = norma(Project1.in_degree_distribution(dpa))
    plot(normed, 'DPA-generated', subplot, filename)

def main():
    # plot all graphs individually
    question1(None, '1-citation.png')
    plt.clf()
    question2(None, '2-random.png')
    plt.clf()
    question3(None, '3-dpa.png')

    # plot all three graphs on a single plot
    plt.clf()
    plt.cla()
    question1(311)
    question2(312)
    question3(313, 'citation-random-dpa.png')

    # plot two graphs on a single plot and show it
    plt.clf()
    plt.cla()
    question1(211)
    question3(212, 'citation-dpa.png')
    plt.show()


if __name__ == '__main__':
    main()
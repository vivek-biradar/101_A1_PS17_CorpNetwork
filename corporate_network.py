import csv


# data structure to store graph edges
class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


class Graph:
    # Constructor
    def __init__(self, edges, N):
        # allocate memory for the adjacency list
        self.adj = [[] for _ in range(N)]

        # add edges to the undirected graph
        for current in edges:
            # allocate node in adjacency List from src to dest
            self.adj[current.src].append(current.dest)


# print adjacency list representation of graph
def printGraph(graph):
    for src in range(len(graph.adj)):
        # print current vertex and all its neighboring vertices
        for dest in graph.adj[src]:
            print(f"({src} -> {dest}) ", end="")
        print()





class CorporateNetwork():
    DirectorCompany = []  # list containing companies and directors
    edges = [[], []]  # matrix of edges/ associations

    def readCompanyDirfile(self, inputfile):
        DirectorCompany=[]
        edges=[]
        with open(inputfile, 'r') as fp:
            Lines = fp.readlines()
            for line in Lines:
                list_comp_dir=line.rstrip('\n').split(' / ')
                company = list_comp_dir[0]
                for val in list_comp_dir:
                    DirectorCompany.append(val)
                    if val == company:
                        continue
                    edges.append((val, company))
            nodes=list(set(DirectorCompany))
        return edges,nodes




if __name__ == '__main__':
    corp=CorporateNetwork()
    edges1,nodes=corp.readCompanyDirfile('inputPS17.txt')
    print(edges1)
    print(nodes)
'''
    edges=[]
    for edge1 in edges1:
        edges.append(Edge(edge1[0],edge1[1]))
    print(edges)
        #Edge(edge1[0],edge1[1])


    # Input: Edges in a directed graph
    #edges = [Edge(0, 1), Edge(1, 2), Edge(2, 0), Edge(2, 1),Edge(3, 2), Edge(4, 5), Edge(5, 4)]

    #Input: No of vertices
    N = len(nodes)

    #construct graph from given list of edges
    graph = Graph(edges, N)

    #print adjacency list representation of the graph
    printGraph(graph)


    def displayAll(self):
        print(total_number_of_companies)
        print(total_number_of_directors)
        print('List of companies')
        for company_name in list_of_companies:
            print(company_name)
        print('List of Directors')
        for director_name in list_of_directors:
            print(director_name)
        pass

    def displayCompanies(self, Director):
        pass

    def displayDirectors(self, Company):
        pass

    def findCommonDirector(self, CompanyA, CompanyB):
        pass

    def findRelatedCompany(self, CompanyA, CompanyB):
        pass


if __name__ == "__main__":
    with open('inputps17.txt','r') as f:
        company_name = [row[0] for row in csv.reader(f,delimiter='/')]
        print(company_name)
    corpNet = CorporateNetwork()
    
'''

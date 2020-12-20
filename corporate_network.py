import sys

sys.stdout = open("outputPS17.txt", "w")
class Node():

    def __init__(self, node_label, type):
        self.node = node_label
        self.type = type


    def __eq__(self, other):
        return self.node == other.node

    def __str__(self):
        return self.node


class CorporateNetwork():
    DirectorCompany = []  # list of Node Objects containing companies and directors
    edges = []  # matrix of edges/ associations

    def printAdjList(self):

        print("*****************Graph Adjacency List**********************")

        for graph_node in self.DirectorCompany:
            indx = self.DirectorCompany.index(graph_node)
            print("{}-> {}".format(graph_node.node, self.edges[indx]))

    def displayAll(self):

        print("********************DISPLAY ALL**************************")
        totalcomp = 0
        totaldirectors = 0
        companyList = []
        directorList = []

        if (len(self.DirectorCompany) == 0):
            print("The graph is empty")
        else:
            for graph_node in self.DirectorCompany:
                if (graph_node.type == "Company"):
                    totalcomp = totalcomp + 1
                    companyList.append(graph_node.node)
                else:
                    totaldirectors = totaldirectors + 1
                    directorList.append(graph_node.node)

            print("Total no. of Companies:{}".format(totalcomp))
            print("Total no. of Directors:{}".format(totaldirectors))
            print("List of Companies:")
        print(*companyList, sep="\n")
        print("List of Directors:")
        print(*directorList, sep="\n")

    def displayCompanies(self, Director):

        print("*****************DISPLAY COMPANIES**************************")

        try :
            director_node = Node(Director, "Director")
            indx = self.DirectorCompany.index(director_node)
            print("Director name:{}".format(Director))
            print("List of Companies:")
            print(self.edges[indx], sep="\n")
        except ValueError as e :
            print("Error : Director {} does not exist in the graph".format(Director))

    def displayDirectors(self, Company):

        print("*****************DISPLAY DIRECTORS**************************")

        try :
            comp_node= Node(Company, "Company")
            indx = self.DirectorCompany.index(comp_node)
            print("Company name:{}".format(Company))
            print("List of Directors:")
            print(*set(self.edges[indx]), sep="\n")
        except ValueError as e :
            print("Error : Company {} does not exist in the graph".format(Company))

    def getAdjacencyList(self, node):

        try :
            input_node= Node(node, "")
            indx = self.DirectorCompany.index(input_node)
            return set(self.edges[indx])
        except ValueError as e :
            print("Error : Node {} does not exist in the graph".format(node))

    def getCompanies(self, Director):

        print("*****************DISPLAY DIRECTORS**************************")

        try :
            director_node= Node(Director, "Director")
            indx = self.DirectorCompany.index(director_node)
            set(self.edges[indx])
        except ValueError as e :
            print("Error : Director {} does not exist in the graph".format(Director))

    def findCommonDirector(self, CompanyA, CompanyB):

        print("*****************FIND COMMON DIRECTORS**************************")

        print("Company A:{}".format(CompanyA))
        print("Company B:{}".format(CompanyB))
        compAindx = self.DirectorCompany.index(Node(CompanyA, "Company"))
        compBindx = self.DirectorCompany.index(Node(CompanyB, "Company"))


        compADirectors = set(self.edges[compAindx])
        compBDirectors = set(self.edges[compBindx])

        if (compADirectors & compBDirectors):
            print("Related: Yes,{}".format(*list(compADirectors & compBDirectors)),sep=":")
        else:
            print("Companies {} and {} have no common directors".format(CompanyA,CompanyB))


    def bfs(self,startNode,endNode):

        visited_node = []
        to_visit_node = []

        # Start with Company A
        to_visit_node.append(startNode)
        visited_node.append(startNode)

        while (len(to_visit_node) > 0):

            s = to_visit_node.pop(0)
            adj_list = self.getAdjacencyList(s)

            for curr_node in adj_list:
                if (curr_node not in visited_node):
                    if (curr_node == endNode):
                        return True
                    visited_node.append(curr_node)
                    to_visit_node.append(curr_node)

        return False


    def findRelatedCompany(self, CompanyA, CompanyB):

        print("*****************FIND RELATED COMPANY**************************")

        print("Company A:{}".format(CompanyA))
        print("Company B:{}".format(CompanyB))

        res = self.bfs(CompanyA,CompanyB)
        if(res):
            print("Related:Yes")
        else:
            print("Related:No")


    def readCompanyDirfile(self, inputfile):
        with open(inputfile, 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                inputList = line.rstrip('\n').split(" / ")
                comp_name = inputList[0].rstrip(" ")
                comp_node = Node(comp_name,"Company")
                try:
                    indx = self.DirectorCompany.index(comp_node)
                    self.edges[indx].append(inputList[1:])
                except ValueError as e:
                    self.DirectorCompany.append(comp_node)
                    indx = len(self.DirectorCompany) - 1
                    self.edges.insert(indx, inputList[1:])

                for director in inputList[1:]:
                    director_node = Node(director.rstrip(" "), "Director")
                    try:
                        indx = self.DirectorCompany.index(director_node)
                        self.edges[indx].append(inputList[0])
                    except ValueError as e:
                        self.DirectorCompany.append(director_node)
                        indx = len(self.DirectorCompany) - 1
                        self.edges.insert(indx, [comp_name])


if __name__ == '__main__':
    corp = CorporateNetwork()
    corp.readCompanyDirfile('inputPS17.txt')
    #corp.printAdjList()
    corp.displayAll()
    corp.displayCompanies("Maria Garcia")
    corp.displayDirectors("ABCD Corp")
    corp.findCommonDirector("ABCD Corp","HAHAHA Laughing Corp")
    corp.findRelatedCompany("ABCD Corp", "Assignment 17")



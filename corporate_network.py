class Node():

    def __init__(self, NodeLabel, Type):
        self.NodeL = NodeLabel
        self.Type = Type

    def __eq__(self, other):
        return self.NodeL == other.NodeL

    def __str__(self):
        return self.NodeL


class CorporateNetwork():
    DirectorCompany = []  # list containing companies and directors
    edges = []  # matrix of edges/ associations

    def printGraph(self):

        print("*****************Graph Adjacency List**********************")

        for node in self.DirectorCompany:
            indx = self.DirectorCompany.index(node)
            print("{}-> {}".format(node.NodeL, self.edges[indx]))

    def displayAll(self):

        print("********************DISPLAY ALL**************************")
        totalcomp = 0
        totaldirectors = 0
        companyList = []
        directorList = []

        if (len(self.DirectorCompany) == 0):
            print("The graph is empty")
        else:
            for node in self.DirectorCompany:
                if (node.Type == "Company"):
                    totalcomp = totalcomp + 1
                    companyList.append(node.NodeL)
                else:
                    totaldirectors = totaldirectors + 1
                    directorList.append(node.NodeL)

            print("Total no. of Companies:{}".format(totalcomp))
            print("Total no. of Directors:{}".format(totaldirectors))
            print("List of Companies:")
        print(*companyList, sep="\n")
        print("List of Directors:")
        print(*directorList, sep="\n")

    def displayCompanies(self, Director):

        print("*****************DISPLAY COMPANIES**************************")

        indx = self.DirectorCompany.index(Node(Director, "Director"))
        print("Director name:{}".format(Director))
        print("List of Companies:")
        print(*set(self.edges[indx]), sep="\n")

    def displayDirectors(self, Company):

        print("*****************DISPLAY DIRECTORS**************************")

        indx = self.DirectorCompany.index(Node(Company, "Company"))
        print("Company name:{}".format(Company))
        print("List of Directors:")
        print(*set(self.edges[indx]), sep="\n")


    def readCompanyDirfile(self, inputfile):
        with open(inputfile, 'r') as fp:
            Lines = fp.readlines()
            for line in Lines:
                inputList = line.rstrip('\n').split(" / ")
                try:
                    indx = self.DirectorCompany.index(Node(inputList[0].rstrip(" "), "Company"))
                    self.edges[indx].append(inputList[1:])
                except ValueError as e:
                    self.DirectorCompany.append(Node(inputList[0].rstrip(" "), "Company"))
                    indx = self.DirectorCompany.index(Node(inputList[0].rstrip(" "), "Company"))
                    self.edges.insert(indx, inputList[1:])

                for director in inputList[1:]:
                    try:
                        indx = self.DirectorCompany.index(Node(director.rstrip(" "), "Director"))
                        self.edges[indx].append(inputList[0])
                    except ValueError as e:
                        self.DirectorCompany.append(Node(director.rstrip(" "), "Director"))
                        indx = self.DirectorCompany.index(Node(director.rstrip(" "), "Director"))
                        self.edges.insert(indx, [inputList[0]])


if __name__ == '__main__':
    corp = CorporateNetwork()
    corp.readCompanyDirfile('inputPS17.txt')
    corp.printGraph()
    corp.displayAll()
    corp.displayCompanies("Maria Garcia")
    corp.displayDirectors("ABCD Corp")


import csv


class CorporateNetwork():
    DirectorCompany = []  # list containing companies and directors
    Edges = [[], []]  # matrix of edges/ associations

    def readCompanyDirfile(self, inputfile):
        with open(inputfile, 'r') as f:
            company_name = [row[0] for row in csv.reader(f, delimiter='/')]
            print(company_name)

        pass

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
    


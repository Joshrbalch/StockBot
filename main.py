from functions import *
from randModule import *
from writeJSON import *

print_hello()
companies = readInCompanies()
printPriceAvg(companies)
writeJSON("Apple", 1, 2, randomize())
writeJSON("Google", 5, 6, randomize())
import json
from pprint import pprint

class Company:
   name = ""
   ticker = ""
   initialPrice = 0
   price2002 = 0
   price2007 = 0
   price2012 = 0

def print_hello():
    print("Hello, World!")

def printCompanies():
  with open('C:\\Users\\joshr\\Documents\\GitHub\\StockBot\\sample-stocks-data.json') as user_file:
    file_contents = json.load(user_file)
  
  pprint(file_contents)

def printPriceAvg(companies):
    total_price = 0
    for company in companies:
        total_price += company["initialPrice"]

    average_price = total_price / len(companies)
    print(average_price)


def readInCompanies():
    with open('C:\\Users\\joshr\\Documents\\GitHub\\StockBot\\sample-stocks-data.json') as user_file:
        file_contents = json.load(user_file)

    # Accessing the list of companies
    companies_data = file_contents  # since "companies" is already the root

    # List to store company instances or dictionaries
    companies = []

    # Iterating through the companies and printing their names and prices
    for company_data in companies_data:
        # Assuming you want to create a dictionary for each company
        company = {
            "name": company_data["company"],
            "description": company_data["description"],
            "initialPrice": company_data["initial_price"],
            "price2002": company_data["price_2002"],
            "price2007": company_data["price_2007"],
            "symbol": company_data["symbol"]
        }

        # Append the company data to the list
        companies.append(company)

    # Print the list of companies
    return companies

# Call the function to read in companies
readInCompanies()




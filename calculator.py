"""
Calculator by Cody Bernardy www.bernardy.biz
"""
import math 
from sys import exit 

def loan():
	print("What was the loan amount?")
	loanAmount = raw_input("> ")
	print("What is the interest rate in (whole number amount)?")
	interestRate = raw_input(" ")
	print("Points charged by lender(if you don't know what points are, check out our defintions tab)")
	pointsCharged = raw_input("> ")
	print("Interest only loan? (See definitions)")
	income()

def income():
	print("Gross monthly income")
	grossIncome = raw_input("> ")
	print("What Landlord expenses do you have monthly?")
	print("1. Electricity")
	electricity = raw_input("> ")
	print("2. Water")
	water = raw_input("> ")
	print("3. PMI")
	pmi = raw_input("> ")
	print("4. Garbage")
	garbage = raw_input("> ")
	print("5. HOA")
	hoa = raw_input("> ")
	print("6. Insurance")
	insurance = raw_input("> ")
	print("7. Taxes")
	taxes = raw_input("> ")
	print("8. Vacancy")
	vacancy = raw_input("> ")
	print("9. Repairs")
	repairs = raw_input("> ")
	print("10. Capital Expenditures")
	CAPEX = raw_input("> ")
	print("11. Property Management")
	propertyManagement = raw_input("> ")

	netIncome = grossIncome - electricity - water - pmi - garbage - hoa - insurance - taxes - vacancy - repairs - CAPEX - propertyManagemen

	print("After expenses, your monthly income is:${0}").format(netIncome)
			
def rentalProperty():
	print("Report Title")
	reportTitle = raw_input("> ")
	print("Property Address:")
	propertyAddress = raw_input("> ")
	print("Annaul Property Taxes")
	annualPropertyTax = raw_input("> ")
	print("MLS Number")
	MLS = raw_input("> ")
	print("Original purchase price")
	purchasePrice = raw_input("> ")
	print("After Repair Value")
	afterRepair = raw_input("> ")
	print("Estimated Closing Costs")
	closingCosts = raw_input("> ")
	print("Repair Costs")
	repairCosts = raw_input("> ")
	print("Was this a cash purchase?")
	cashPurchase = raw_input("> ")

	if cashPurchase == "Yes" or "yes" or "YES":
		income()

	elif cashPurchase == "No" or "no" or "NO":
		loan()

def openingScreen():
	print("Welcome to the Real Estate Calculator")
	print("1. Rental Property Calculator")
	print("2. House Flipping Calculator")
	print("3. Definitions")
	print " "
	print("Enter the number of the calculator you want to use.")
	userInput = raw_input("> ")

	if userInput == "1":
		rentalProperty()
	elif userInput == "2":
		flipProperty()
	elif userInput == "3":
		definitions()
	else:
		exit()

print openingScreen()
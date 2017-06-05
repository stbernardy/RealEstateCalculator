"""
Calculator by Cody Bernardy www.bernardy.biz
"""
import math 
from sys import exit 

def getinput(questions):
	out=[]
	for quest in questions:
		print quest
		out.append(int(raw_input("> ")))
	return out

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
	incomequest=[
	"Gross monthly income",
	"What Landlord expenses do you have monthly?\n1. electricity",
	"2. water",
	"3. PMI",
	"4. Garbage",
	"5. HOA",
	"6. Insurance",
	"7. Taxes",
	"8. Vacancy",
	"9. Repairs",
	"10. Capital Expenditures",
	"11. Property Management",
	]

	netIncome = getinput(incomequest)

	print("After expenses, your monthly income is:${0}").format(netIncome[0]-sum(netIncome[1:]))
			
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

	if cashPurchase.lower() == "yes":
		income()

	elif cashPurchase.lower() == "no":
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
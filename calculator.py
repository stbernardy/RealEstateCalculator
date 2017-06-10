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

	if interestOnly.lower() == "yes":
		income()
	elif interestOnly == "no" or "No":
		pass	
	loanQuestions=[
	"What was the loan amount?",
	"What is the interest rate? (In a whole number)",
	"Points charged by the lender(if you do not know what points are, check out our defintions tab)",
	]


def income():
	incomequest=[
	"Gross monthly income",
	"What Landlord expenses do you have monthly?\n1. Electricity",
	"2. Water",
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
	rentalQuest=[
	"What is theProperty Address",
	"Report Name",
	"What is the Annual Property Tax?",
	"What is the MLS number?",
	"What was the Original Purchasing Price?",
	"What is the After Repair Value?",
	"What is the Estimated Closing Costs?",
	]

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

openingScreen()

print("Was this a cash purchase?")
cashPurchase = raw_input("> ")

if cashPurchase.lower() == "yes":
	income()

elif cashPurchase.lower() == "no":
	loan()


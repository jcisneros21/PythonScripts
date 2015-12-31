import sys

buyerInfo = "Buyer's name: "
buyerNum = "Buyer's number: "
sellerInfo = "Seller's name: "
sellerNum = "Seller's number: "
agentInfo = "Transaction's Agent: "
addressInfo = "Property's Address: "
priceInfo = "Property's Price: "
paidInfo = "Commission Received: "
extraInfo = "Extra Revenue Received: "
otherInfo = "Other Information: \n"

def reading():
	readFile = open('Client_Info.txt')
	hello = readFile.read()
	print(hello)
	readFile.close()
	
def writing(user_input):
	writeFile = open('Client_Info.txt','a')
	writeFile.write(user_input + '\n')
	writeFile.close()

def headers(date):
	ast = '*' * 15
	headerFile = open('Client_Info.txt','a')
	headerFile.write(ast + ' ' +  date + ' ' + ast + '\n')
	headerFile.close()
	
def space():
	endFile = open('Client_Info.txt','a')
	endFile.write('\n')
	endFile.close()

def totalPrice():
	amount = 0
	totalFile = open('Client_Info.txt')
	content = totalFile.readlines()
	for data in content:
		if data[0:18] == "Property's Price: ":
			data = data.replace(",","")
			data = data.replace(".00","")
			amount += int(data[18:].strip('\n'))
	totalFile.close()
	return str(amount)

def commission():
	amount = 0
	comFile = open('Client_Info.txt')
	content = comFile.readlines()
	for data in content:
		if data[0:21] == 'Commission Received: ':
			data = data.replace(",","")
			data = data.replace(".00","")
			amount += int(data[21:].strip('\n'))
	comFile.close()
	return str(amount)
	
def extraRevenue():
	amount = 0
	extraFile = open('Client_Info.txt')
	content = extraFile.readlines()
	for data in content:
		if data[0:23] == 'Extra Revenue Received:':
			data = data.replace(",","")
			data = data.replace(".00","")
			amount += int(data[23:].strip('\n'))
	extraFile.close()
	return str(amount)
			
def currentDate():
	year = input('Please enter the Year: ')
	month = input('Please enter the Month: ')
	day = input('Please enter the Day: ')
	date = month + ' ' + day + ', ' + year
	return date

def clientInfo():
	buyer = input('Please enter the name of the buyer: ')
	buyer = buyerInfo + buyer
	bNumber = input('Please enter the phone number of the buyer: ')
	bNumber = buyerNum + bNumber
	seller = input('Please enter the name of the seller: ')
	seller = sellerInfo + seller
	sNumber = input('Please enter the phone number of the seller: ')
	sNumber = sellerNum + sNumber
	agent = input('Please enter the name of the transaction agent: ')
	agent = agentInfo + agent
	address = input('Please enter the address of the property: ')
	address = addressInfo + address
	price = input('Please enter the price of the property: ') 
	price = priceInfo + price
	paid = input('Please enter the commission recieved: ')
	paid = paidInfo + paid
	extra = input('Please enter extra revenue: ')
	extra = extraInfo + extra
	print('Any other information: ')
	other = input()
	other = otherInfo + other
	
	info = [buyer,bNumber,seller,sNumber,agent,address,price,paid,extra,other]
	for i in info:
		writing(i)

print("This is the extra commission: " + totalPrice())
while True:
	headers(currentDate())
	space()
	clientInfo()
	print()
	space()
	answer = input('Would you like to add another transaction?(Y/N): ')
	if answer != 'Y':
		sys.exit(0)
	
#currency converter
with open('currencydata.txt') as f:
    lines=f.readlines()

currencydict={}
for line in lines:
    separate = line.split('\t')
    currencydict[separate[0]]=separate[1]

amount=int(input("Enter amount of money:"))
print("The name of currency")
[print(item)for item in currencydict.keys()]
currency=input("Please select one of the currency:")
print(f"{amount}THB = {amount /float(currencydict[currency])}{currency} ")
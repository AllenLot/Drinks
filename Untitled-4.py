#Name: Allen Loten
#Email: allen.loten46@myhunter.cuny.edu

def computePrice():
    price=0
    drink = input("Drink: ")
    size = input("Size: ")
    if size == "coffee" or size == "misto" or size == "mocha" or size == "tea":
        drink(size, drink)
    else:
        print(size, "size", drink + ":", -1)

def coffee(size, drink):
    if size == "small":
        price = 2.5
    if size == "medium":
        price = 2.75
    if size == "large":
        price = 3.00
def misto(size, drink):
    if size == "small":
        price = 3.15
    if size == "medium":
        price = 3.35
    if size == "large":
        price = 3.7
def mocha(size, drink):
    if size == "small":
        price = 3.5
    if size == "medium":
        price = 3.8
    if size == "large":
        price = 4.25
def tea(size, drink):
    if size == "small":
        price = 2.35
    if size == "medium":
        price = 2.45
    if size == "large":
        price = 2.90
    print(size, "size", drink + ":", price)

if __name__ == '__main__':
    computePrice()

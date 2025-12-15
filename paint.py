#1st function
def main():
    feetWall = 0.0
    paintPri = 0.0
    
    gallonP = 0.0
    laborh = 0.0
    paintc = 0.0
    laborc = 0.0
    GALLONF = 112
    HLABOR = 8
    CHARGE = 35.00
    #Prompts user to ask for amount of wall space and paint price
    feetWall, paintPri = info(feetWall, paintPri)
    print(feetWall)
    print(paintPri)

    gallonP = int(feetWall / GALLONF) + 1

    laborh = gallonP * HLABOR

    laborc = laborh * CHARGE

    paintc = gallonP * paintPri


    showCost(gallonP, laborh, paintc, laborc)
#2nd function
def showCost(a, b, c, d):
    total = 0.0

    total = c + d


    print("Paint gallons: ", a)
    print("Labor hours: ", b)
    print("Charges for paint: $" ,\
          format(c, ',.2f'), sep='')
    print("Charges for labor: $" ,\
          format(d, ',.2f'), sep='')
    print("Total: $",\
          format(total, ',.2f'), sep='')

def info(x, y):
    x = float(input("Enter the wall space in sq feet: "))

    y = float(input("Enter the price of the paint per gallon: "))
    
    return x, y

main()


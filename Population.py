pop = int(input("How many organisms are present?"))
dail = int(input("What is the daily increase in percentage?"))
muti = int(input("How many days did they multiply?"))
print("Days\tPopulation")

dail = dail / 100

for k in range(muti):
    print(k + 1,'\t', "{:.3f}".format(pop))


    pop += pop * dail
    

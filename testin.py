#Man I haven't worked on python in a minute so im a bit rusty ;D

print("Dragon ball character quiz 1")
print("For the most hardcore fans to answer")
print("\n")
dbq1 = str(input("Who is the main character? Select from 4 choices" "\n" "A. Goku  B. Vegeta  C. Gohan  D. Piccolo"))
while dbq1.upper() != "A" or dbq1.upper() !=  "B" or dbq1.upper() !=  "C" or dbq1.upper() !=  "D":
    print("That's NONE of the options!, Try again!")
    dbq1 = str(input("Who is the main character? Select from 4 choices" "\n" "A. Goku  B. Vegeta  C. Gohan  D. Piccolo"))



    
if dbq1.upper() == "A":
             print("Correct!!")
elif dbq1.upper() ==  "B":
    print("Wrong!! Veegta gets hoed every fight, he's DEFINETLEY not the MC")
elif dbq1.upper() == "C":
    print("Wrong!! Thats Goku's son, the son of the MC isn't an MC, but a strong support")
elif dbq1.upper() == "D":
    print("Wrong!! Piccolo is my favorite but sadly not the MC. :(")    


dbq2 = str(input("Who is the (regular) fusion of Goku and Vegeta?" "\n" "A. Vegito  B. Gotenks  C. Gogito  D. Gogeta "))

if dbq2.upper() == "A":
          print("Wrong!! That's the POTARA fusion, not the regular fusion")
elif dbq2.upper() == "B":
    print("Wrong!! Tha's not even a Goku and Vegeta fusion, thats the fusion of their sons!")
elif dbq2.upper() == "C":
    print("Wrong!! That fusion doesn't even EXIST! (yet)")
elif dbq2.upper() == "D":
    print("Correct!!")


import dogBreath as CD

pet: CD.dogBreath
pets: list()

for i in range(5):
    pet = CD.dogBreath()
    pets.append(pet)

for myPet in pets:
    print('my pet name is:',  myPet.getName())
    print('my pet has a tail :', str(myPet.hasTail))
    myPet.speak()

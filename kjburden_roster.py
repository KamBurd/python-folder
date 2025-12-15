#  NCAT Kameron Burden
#  COMP-163 : Section 01
#  Instructor : Derrick Leflore
#  Description : Apphending a list of names to a text file.
# naming convention : kjburden_roster.py

 

#Apphends the text file
fileHandle = open("Roster.txt", "a")

#Prompts the user to enter a name (firstname and lastname)
write = input('Enter a name, make sure it\'s the first and last name. ex: Kameron Burden is one whole name. ')

#Writes the text entered by the user into the text file
fileHandle.write(write)

#Makes a new line so that the next name is on a different line from the previous text
fileHandle.write('\n')

#The user will continue to be prompted to enter a name, until they enter the character 'q' to end the loop
while True:
        write = input('Enter a name, make sure its the first and last name. enter the character \'q\' by itself on this prompt to exit the code ')
        if write == 'q':
            break
        else:
            
            fileHandle.write(write)
            fileHandle.write('\n')

#Closes the text file.
fileHandle.close()
 

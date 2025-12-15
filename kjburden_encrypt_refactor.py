#Name: Kameron Burden
#Date: 10/6/2022
#Class: COMP163001.202310
#This program is meant to prompt the user to enter characters to be encoded, then prompt again for the text to be decoded


#decoding function with recursive
def deco(message, po, length):
    if po > (length-1):
        return
    print(list(encodeDic.keys())[list(encodeDic.values()).index(msg[po])]
    po += 1
    deco(message, po, length)


    
#encoded messages dictonary
encodeDic = {" " : "^", "a": "&" , "b": "$", "c": "!", "d": ".", "e": "3", "f": "?", "g": "*", "h": "*", "i": "<", "j": "8", "k": "@",
             "l": "#", "m": "2", "n": "'", "o": "{", "p": "}", "q": "~", "r" : "`", "s": ":", "t": ";", "u": "[", "v": "]", "w": ">",
             "x": ",", "y": "/", "z": "."}

encodeMsg = ''
#prompts user to enter a text message
textMsg = input("Enter text message : ").lower()

for text in textMsg:
    encodeMsg += str(encodeDic.get(text))
#prints encoded text
print(encodeMsg)
print()
#prompts user for encoded text to decode it
textMsg = input("Enter encoded text for decode ")
decodeMsg = ''
for text in textMsg:
    for key, value in encodeDic.items():
        if text == value:
            decodeMsg += key
#prints decoded text.
print(decodeMsg)


    

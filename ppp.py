encodeDic = {" " : "^", "a": "&" , "b": "$", "c": "!", "d": ".", "e": "3", "f": "?", "g": "*", "h": "*", "l": "<", "j": "8", "k": "@",
             "l": "#", "m": "2", "n": "'", "o": "{", "p": "}", "q": "~", "r" : "`", "s": ":", "t": ";", "u": "[", "v": "]", "w": ">",
             "x": ",", "y": "/", "z": "."}
textMsg = input("Enter text message :")
encodeMsg = ''
for i in textMsg:
    encodeMsg += encodeDic.get(i)
print(encodeMsg)
for i in encodeMsg:
    if encodeMsg in encodeDic:
        encodeMsg = textMsg
print(encodeMsg)
    
    

    

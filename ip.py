filename = input()

data = []
with open(filename, 'w') as file:
    
    res = file.read()
    data = res.split(" ")
    file.close()
    
for i,filename in enumerate(data):
    data[i] = filename.replace("_photo.jpg","_info.txt")
    
#print modified data

print(" ".join(data))
 

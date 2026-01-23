f=open("myfile.txt","r")
print("cursor positon:-",f.tell())
f.read(3)
print("cursor position:-",f.tell())
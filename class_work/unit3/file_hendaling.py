# f=open("text.txt","w")
# f.write("Everything")
# f.close()

# f=open("text.txt","w")
# l=["python\n","java\n","php\n","android\n"]
# f.writelines(l)
# f.close()

# f=open("text.txt","a")
# f.write("something..")
# f.close()

# f=open("text.txt","r")
# data =f.close()
# print(data)

# f=open("text.txt","r")
# data = f.readlines()
# print(data)
# f.close()

# f=open("text.txt","r")
# data = f.read()
# if not data:
#     print("file empty")
# f.close()

# f=open("text.txt","r")
# while True:
#     data = f.readline()
#     if "a" in data.lower():
#         print(data)
#     if not data:
#         break
# f.close()

# with open("home.txt","w+") as f:
#     f.write("hello python")
#     f.seek(0)
#     data = f.read()
#     print(data)

# with open("home.txt","r+") as f:
#     f.write("hello world")
#     f.seek(4)
#     data = f.read()
#     print(data)

import json
d = {
    "name":"sneha",
    "email":"sneha@gmail.com",
    "phone":"1234567890"
}
with open("data.json","w") as f:
    json.dump(d,f)


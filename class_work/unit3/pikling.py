import pickle
st={
    "name":"sneha",
    "email":"s@gmail.com",
    "phone":"1234567890"
}

with open('obj.pkl','wb') as f:
    pickle.dump(st,f)
    print("sucess")


with open('obj.pkl','rb') as f:
    data=pickle.load(f)
    print(data)
